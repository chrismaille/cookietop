from dataclasses import dataclass
from typing import Dict, Any, Optional, List, Type

from aws_lambda_context import LambdaContext
from marshmallow import Schema


@dataclass
class Request:
    """Request Object.

    This request object will be inject
    in all view handlers.

    Properties
    ==========

        original_body:  Original body received in AWS event, if available
        body:           Converted body to dictionary, if available
        validated_data: Body validated by a marshmallow schema,
                        informed in `handler_view` decorator.
        aws_event:      Original AWS Event
        aws_context:    Original AWS Context
        path:           Path Parameters from AWS Context
        headers:        Header Parameters from AWS Context
        authorizer:     Authorization Data from Profile
        original_body:      Original body received in AWS event, if available
        body:               Converted body to dictionary, if available
        validation_errors:  Validation errors as per marshmallow schema,
                            informed in `handler_view` decorator.
        schema:             Marshmallow schema used in validation.
        aws_event:          Original AWS Event
        aws_context:        Original AWS Context
        path:               Path Parameters from AWS Context
        headers:            Header Parameters from AWS Context
        authorizer:         Authorization Data from Profile
    """

    validation_errors: Optional[Dict[str, List[str]]]
    aws_event: Dict[Any, Any]
    aws_context: LambdaContext
    original_body: Optional[str] = None
    body: Optional[Dict[Any, Any]] = None
    path: Optional[Dict[Any, Any]] = None
    headers: Optional[Dict[Any, Any]] = None
    authorizer: Optional[Dict[Any, Any]] = None
    schema: Optional[Type[Schema]] = None
