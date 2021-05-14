import json

import arrow
import pytest
from aws_lambda_context import LambdaContext
from stela import settings

from handlers.health import health_check
from helpers.status_code import StatusCode


@pytest.mark.freeze_time("2021-05-05 12:00:01")
def test_health_check():
    response = health_check({}, LambdaContext())
    expected_response = {
        "statusCode": StatusCode.OK.value,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(
            {
                "status": "OK",
                "project": settings["project.name"],
                "environment": settings.stela_options.current_environment,
                "datetime": arrow.utcnow().isoformat(),
            }
        ),
    }

    assert response == expected_response
