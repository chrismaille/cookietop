from dataclasses import dataclass
from typing import Dict, Any, Optional

from aws_lambda_context import LambdaContext


from initializers.sql import Session


@dataclass
class Request:
    """Request Object.

    This request object will be inject
    in all view handlers.

    Properties
    ==========

        db_session:     Current database session
        original_body:  Original body received in AWS event, if available
        body:           Converted body to dictionary, if available
        validated_data: Body validated by a marshmallow schema,
                        informed in `handler_view` decorator.
        aws_event:      Original AWS Event
        aws_context:    Original AWS Context

    Examples
    ========

    1. Case use: Simple POST
    aws_event = {"foo": "bar"}

    >>> from helpers.types import HandlerResponse
    >>> from helpers.decorators import handler_view
    >>> from helpers.status_code import StatusCode
    >>>
    >>> # aws_event = "{\"foo\": \"bar\"}"
    >>> @handler_view()
    >>> def post_foo(request: Request) -> HandlerResponse:
    >>>    return {
    >>>        "message": {
    >>>            "original_body": request.original_body,  # "{\"foo\": \"bar\"}"
    >>>            "body": request.body,  # dict(foo="bar")
    >>>            "validated_data": None, # No schema informed
    >>>        },
    >>>        "status_code": StatusCode.OK
    >>>    }

    2. Case use: POST with Marshmallow Schema

    >>> from helpers.types import HandlerResponse
    >>> from helpers.decorators import handler_view
    >>> from helpers.status_code import StatusCode
    >>> from marshmallow import fields, Schema
    >>>
    >>> class FooSchema(Schema):
    >>>     foo = fields.Float(required=True)
    >>>
    >>> # aws_event = "{\"number\": \"1\"}"
    >>> @handler_view(schema=FooSchema)
    >>> def post_foo(request: Request) -> HandlerResponse:
    >>>    return {
    >>>        "message": {
    >>>            "original_body": request.original_body,  # "{\"number\": \"1\"}"
    >>>            "body": request.body,  # dict(number="1")
    >>>            "validated_data": {"number": 1.0}
    >>>        },
    >>>        "status_code": StatusCode.CREATED
    >>>    }

    """

    db_session: Session
    validated_data: Dict[Any, Any]
    original_body: Optional[str]
    body: Optional[Dict[Any, Any]]
    aws_event: Dict[Any, Any]
    aws_context: LambdaContext
