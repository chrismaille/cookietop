"""Request Based Lambda Authorizer.

As per: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html  # noqa: E501
And https://github.com/awslabs/aws-apigateway-lambda-authorizer-blueprints/blob/master/blueprints/python/api-gateway-authorizer-python.py  # noqa: E501
"""
from loguru import logger
from stela import settings

from interface.aws.exceptions import RequestUnauthorizedError
from interface.aws.generate_iam_policy import generate_iam_policy
from interface.aws.handler_view import handler_view
from interface.aws.request import Request
from interface.types.auth_response import AuthResponse, PolicyEffect


@handler_view(format_response=False)
def authorize(request: Request) -> AuthResponse:
    """Return request IAM policy.

    Check for the 'authorizationToken' in request's Header.

    For this example, token will be compared
    with environment variable from SSM.

    :param: request: Sherlock instance
    :return: HandlerResponse Dict
    """
    logger.debug(request.aws_event)
    logger.debug(request.aws_context)
    try:
        token = request.headers["Authorization"]
    except KeyError:
        raise RequestUnauthorizedError("Unauthorized")

    effect = (
        PolicyEffect.deny
        if token != settings["authorization_token"]
        else PolicyEffect.allow
    )

    method_arn = request.aws_event["methodArn"]
    auth_response = generate_iam_policy("APIToken", effect, method_arn)
    logger.debug(f"IAM policy: {auth_response}")
    return auth_response
