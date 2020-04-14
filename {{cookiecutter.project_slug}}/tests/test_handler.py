import json

from aws_lambda_context import LambdaContext
from stela import settings

from application.handlers.health import health_check
from application.types.status_code import StatusCode


def test_health_check():
    response = health_check({}, LambdaContext())
    expected_response = {
        "statusCode": StatusCode.OK.value,
        "body": json.dumps(
            {"status": "OK", "environment": settings.stela_options.current_environment}
        ),
    }

    assert response == expected_response
