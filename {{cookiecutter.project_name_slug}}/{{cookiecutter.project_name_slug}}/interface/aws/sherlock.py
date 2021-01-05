import json
from dataclasses import dataclass
from typing import Dict, Any, Optional, Type, List

from aws_lambda_context import LambdaContext
from loguru import logger
from marshmallow import Schema

from interface.aws.request import Request


@dataclass
class Sherlock:
    """Converts AWS request data in a Request-like object."""

    event_data: Dict[Any, Any]
    context_data: LambdaContext
    schema: Optional[Type[Schema]] = None
    validation_errors: Optional[Dict[str, List[str]]] = None
    body_data: Optional[Dict[Any, Any]] = None
    authorizer: Optional[Dict[Any, Any]] = None

    def validate_body_data(self) -> None:
        """Do the validation of data from schema, if schema and body have info."""
        request_schema = self.get_schema()
        if self.body_data and request_schema:
            logger.debug(f"Start validating data using {request_schema.__name__}...")
            self.validation_errors = request_schema().validate(self.body_data)

    def get_body(self) -> None:
        """Do decode content from body, if body have info."""
        raw_data = self.event_data.get("body")
        self.body_data = json.loads(raw_data) if raw_data else None
        if self.body_data:
            logger.debug(f"Body received: {self.body_data}")

    def get_schema(self) -> Optional[Type[Schema]]:
        """Return request schema.

        :return: Marshmallow Schema subclass
        """
        return self.schema

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
        self.validate_body_data()
        self.get_authorizer()

        return Request(
            validation_errors=self.validation_errors,
            original_body=self.event_data.get("body"),
            body=self.body_data,
            aws_event=self.event_data,
            aws_context=self.context_data,
            path=self.event_data.get("pathParameters"),
            headers=self.event_data.get("headers"),
            authorizer=self.authorizer,
            schema=self.schema,
        )
