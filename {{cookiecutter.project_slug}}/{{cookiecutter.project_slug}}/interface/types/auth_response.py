from enum import Enum, unique
from typing import List

from typing_extensions import TypedDict


@unique
class PolicyEffect(Enum):
    allow = "Allow"
    deny = "Deny"


class StatementAction(TypedDict):
    Action: str
    Effect: str
    Resource: str


class PolicyDocument(TypedDict):
    Version: str
    Statement: List[StatementAction]


class AuthResponse(TypedDict):
    principalId: str
    policyDocument: PolicyDocument
