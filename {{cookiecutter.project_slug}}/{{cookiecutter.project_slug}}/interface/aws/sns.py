import json
from dataclasses import dataclass
from enum import Enum, unique
from typing import Any

import boto3
from boto3 import Session
from loguru import logger
from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from stela import settings

from enterprise.helpers.get_now import get_now
from enterprise.helpers.get_uuid import get_uuid


@unique
class SNSEventTypes(Enum):
    RegistrationSuccess = "creditcard_creation_success"
    RegistrationFailure = "creditcard_creation_failure"
    PaymentReceived = "payment_received"


class EventMessageData(Schema):
    id = fields.UUID(required=True, default=get_uuid())
    category = fields.String(required=True, default="system")
    type = EnumField(SNSEventTypes, required=True, by_value=True)
    at = fields.DateTime(required=True, default=get_now(), format="%Y-%m-%dT%H:%M:%SZ")
    aggregate_id = fields.String(required=True)
    version = fields.String(required=True, default="1.0")
    payload = fields.Dict(required=True, default={})


@dataclass
class SNSService:
    @property
    def client(self) -> Session.client:
        client = boto3.client("sns")
        return client

    def get_topic_arn(self) -> str:
        topic_name = settings["noverde.topic"]
        topic_arn = [
            topic["TopicArn"]
            for topic in self.client.list_topics()["Topics"]
            if topic_name in topic["TopicArn"]
        ][0]
        logger.debug(f"Find Topic Arn: {topic_arn}")
        return topic_arn

    def publish(self, event: SNSEventTypes, payload: str, aggregate_id: str) -> Any:
        topic_arn = self.get_topic_arn()
        event_data = {"type": event, "aggregate_id": aggregate_id, "payload": payload}
        event_message = json.dumps(
            {"default": EventMessageData().dumps(event_data)}, default=lambda x: str(x)
        )
        logger.debug(f"Message is: {event_message}")

        response = self.client.publish(
            TargetArn=topic_arn,
            Message=event_message,
            MessageStructure="json",
            MessageAttributes={
                "event_type": {"DataType": "String", "StringValue": event.value}
            },
        )
        logger.debug(f"SNS response is: {response}")
        return response
