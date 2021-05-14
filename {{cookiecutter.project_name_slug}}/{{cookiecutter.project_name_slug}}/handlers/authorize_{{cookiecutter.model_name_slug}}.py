from interface.aws.handler_view import view
from interface.aws.request import Request
from interface.aws.policy_generator import PolicyGenerator, Effect
from helpers.handler_response import HandlerResponse
from typing import Any


@view()
def authorize(request: Request, **kwargs: Any) -> HandlerResponse:
    """Lambda Request Authorizer.

    Add here your Authorization logics.

    Default code will always allow requests.

    """
    # token = request.aws_event.get("authorizationToken")
    method_arn = request.aws_event.get("methodArn")

    policy = PolicyGenerator(principal_id="user", resource=method_arn)
    return policy.build(Effect.ALLOW)
