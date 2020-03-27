import json
from dataclasses import dataclass
from typing import Dict, Any, Optional, Type

from loguru import logger
from marshmallow import Schema


@dataclass
class Sherlock:
    event_data: Dict[Any, Any]
    schema: Optional[Type[Schema]] = None
    validated_data: Optional[Any] = None
    body_data: Optional[Dict[Any, Any]] = None

    def get_validated_data_from_schema(self) -> None:
        if self.body_data and self.schema:
            logger.debug(f"Start creating object using {self.schema.__name__}...")
            self.validated_data = self.schema().load(self.body_data)

    def get_body(self) -> None:
        raw_data = self.event_data.get("body")
        self.body_data = json.loads(raw_data) if raw_data else None
        if self.body_data:
            logger.debug(f"Body received: {self.body_data}")

    def inspect(self):
        self.get_body()
        self.get_validated_data_from_schema()
