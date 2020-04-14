from typing import Dict

import pytest

from interface.aws.generate_iam_policy import generate_iam_policy
from interface.types.auth_response import PolicyEffect
from tests.conftest import load_fixture


@pytest.fixture
def accept_iam_policy() -> Dict[str, str]:
    """Accept IAM Policy fixture.

    :return: Dict
    """
    return load_fixture("accept_iam_authorization.json")


def test_generate_iam_policy(accept_iam_policy):
    test_policy = generate_iam_policy(
        user_id="user", effect=PolicyEffect.allow, resource="foo"
    )
    assert test_policy == accept_iam_policy
