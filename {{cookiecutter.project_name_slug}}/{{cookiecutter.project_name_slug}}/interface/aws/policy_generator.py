from enum import Enum, unique
from typing import Any, Dict

from attr import dataclass


@unique
class Effect(Enum):
    ALLOW = "Allow"
    DENY = "Deny"


@dataclass
class PolicyGenerator:
    principal_id: str
    resource: str
    effect: Effect = Effect.DENY

    def build(self, effect: Effect) -> Dict[str, Any]:
        self.effect = effect
        return {"principalId": self.principal_id, "policyDocument": self._make_policy()}

    def _make_policy(self) -> Dict[str, Any]:
        return {"Version": "2012-10-17", "Statement": [self._make_statement()]}

    def _make_statement(self) -> Dict[str, Any]:
        return {
            "Action": "execute-api:Invoke",
            "Effect": self.effect.value,
            "Resource": self.resource,
        }
