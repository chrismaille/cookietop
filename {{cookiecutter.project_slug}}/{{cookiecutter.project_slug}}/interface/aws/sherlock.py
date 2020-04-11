import json
from dataclasses import dataclass
from typing import Dict, Any, Optional, Type

from aws_lambda_context import LambdaContext
from loguru import logger
from marshmallow import Schema

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

    def get_validated_data_from_schema(self) -> None:
        """Do the validation of data from schema, if schema and body have info."""
        if self.body_data and self.schema:
            logger.debug(f"Start creating object using {self.schema.__name__}...")
            self.validated_data = self.schema().load(self.body_data)

    def get_body(self) -> None:
        """Do decode content from body, if body have info."""
        raw_data = self.event_data.get("body")
        self.body_data = json.loads(raw_data) if raw_data else None
        if self.body_data:
            logger.debug(f"Body received: {self.body_data}")

    def inspect(self) -> Request:
        """Inspect and return Request object.

        :return: Request instance
        """
        self.get_body()
        self.get_validated_data_from_schema()
        return Request(
            validated_data=self.validated_data,
            original_body=self.event_data.get("body"),
            body=self.body_data,
            aws_event=self.event_data,
            aws_context=self.context_data,
        )
