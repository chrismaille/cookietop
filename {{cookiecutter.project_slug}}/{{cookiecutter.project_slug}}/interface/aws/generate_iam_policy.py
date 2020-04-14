from interface.types.auth_response import (
    AuthResponse,
    PolicyDocument,
    PolicyEffect,
    StatementAction,
)


def generate_iam_policy(
    user_id: str, effect: PolicyEffect, resource: str
) -> AuthResponse:
    statement_action: StatementAction = {
        "Action": "execute-api:Invoke",
        "Effect": str(effect.value),
        "Resource": resource,
    }
    policy_document: PolicyDocument = {
        "Version": "2012-10-17",
        "Statement": [statement_action],
    }
    auth_response: AuthResponse = {
        "principalId": user_id,
        "policyDocument": policy_document,
    }
    return auth_response
