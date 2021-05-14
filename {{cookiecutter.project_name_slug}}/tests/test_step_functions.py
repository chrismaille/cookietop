import json
from unittest.mock import Mock

from aws_lambda_context import LambdaContext

from handlers.start_demo_machine import start_machine
from interface.aws import step_functions


def test_start_machine_handler(monkeypatch, mocker):
    step_machine = Mock()
    step_machine.list_state_machines.return_value = {
        "stateMachines": [
            {
                "name": "Rage Against The Machine",
                "stateMachineArn": "arn::killing.in.the.name",
            }
        ]
    }
    step_machine.start_execution.return_value = "Lights out! Guerilla Radio!"
    mocker.patch.object(step_functions.boto3, "client", return_value=step_machine)
    monkeypatch.setenv("STEP_MACHINE_NAME", "Rage Against The Machine")

    payload = json.dumps({"Bulls": "On Parade"})
    event = {"body": payload}
    response = start_machine(event, LambdaContext())

    assert response == {
        "statusCode": 200,
        "body": '{"response": "Lights out! Guerilla Radio!"}',
        "headers": {"Access-Control-Allow-Origin": "*"},
    }

    step_machine.start_execution.assert_called_once_with(
        input=payload, stateMachineArn="arn::killing.in.the.name"
    )
