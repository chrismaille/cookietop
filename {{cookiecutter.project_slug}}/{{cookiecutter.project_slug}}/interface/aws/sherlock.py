import json
from dataclasses import dataclass
from typing import Dict, Any, Optional, Type

from aws_lambda_context import LambdaContext
from loguru import logger
from marshmallow import Schema, ValidationError

from enterprise.rulemodels.rule_index import rule_index
from enterprise.types.enterprise_resources import EnterpriseResources
from interface.aws.request import Request


@dataclass
class Sherlock:
    """Do the validation of data schema.

    Inputs are:

        - event_data: receives a dict of any type (int, obj, list, float).
        - schema: receives an optional schema.
        - validated_data: receives an optional data of any type
          (obj, list, float, int).
        - body_data: receives an optional data of dict.
    """

    event_data: Dict[Any, Any]
    context_data: LambdaContext
    schema: Optional[Type[Schema]] = None
    validated_data: Optional[Any] = None
    body_data: Optional[Dict[Any, Any]] = None
    authorizer: Optional[Dict[Any, Any]] = None

    def get_validated_data_from_schema(self) -> None:
        """Do the validation of data from schema, if schema and body have info."""
        request_schema = self.get_schema()
        if self.body_data and request_schema:
            logger.debug(f"Start creating object using {request_schema.__name__}...")
            self.validated_data = request_schema().load(self.body_data)

    def get_body(self) -> None:
        """Do decode content from body, if body have info."""
        raw_data = self.event_data.get("body")
        self.body_data = json.loads(raw_data) if raw_data else None
        if self.body_data:
            logger.debug(f"Body received: {self.body_data}")

    def get_schema(self) -> Optional[Type[Schema]]:
        """Return request schema.

        Find schema if:
            * Explicit defined in View decorator
            * key "rule" in Event body

        This is a very simple example
        to answer the following question:

        * Which Business Rules
        control the instance model we
        will create or update
        in this handler?

        :return: Marshmallow Schema subclass
        """
        if not self.body_data or self.schema:
            return self.schema
        rule = self.body_data.get("rule", None)
        if not rule:
            return None
        try:
            rule_resource = EnterpriseResources[rule]
        except KeyError:
            raise ValidationError(f"Invalid Rule: {rule}.")
        schema = rule_index.get(rule_resource, None)
        logger.debug(f"Schema from Index is: {schema.__name__}")
        return schema

    def get_authorizer(self) -> None:
        """Extract authorizer info, if it exists."""
        request_context = self.event_data.get("requestContext") or {}
        authorizer = request_context.get("authorizer")
        self.authorizer = authorizer if authorizer else None

        if self.authorizer:
            logger.debug(f"Authorizer received: {self.authorizer}")

    def inspect(self) -> Request:
        """Inspect and return Request object.

        :return: Request instance
        """
        self.get_body()
        self.get_validated_data_from_schema()
        self.get_authorizer()

        return Request(
            validated_data=self.validated_data,
            original_body=self.event_data.get("body"),
            body=self.body_data,
            aws_event=self.event_data,
            aws_context=self.context_data,
            path=self.event_data.get("pathParameters"),
            headers=self.event_data.get("headers"),
            authorizer=self.authorizer,
        )
