import json
import os
from dataclasses import dataclass
from typing import Dict, Any

import boto3
from boto3 import Session  # type: ignore
from loguru import logger


@dataclass
class StepMachineService:
    @property
    def client(self) -> Session.client:
        client = boto3.client("stepfunctions")
        return client

    def get_machine_arn(self) -> str:
        state_machine_name = os.getenv("STEP_MACHINE_NAME")
        list_all_machines = self.client.list_state_machines()
        state_machine = [
            machine
            for machine in list_all_machines["stateMachines"]
            if machine["name"] == state_machine_name
        ][0]
        return state_machine["stateMachineArn"]

    def start_execution(self, payload: Dict[Any, Any]) -> Dict[Any, Any]:
        logger.debug(f"Start Send Notification Machine with input: {payload}")
        arn = self.get_machine_arn()
        response = self.client.start_execution(
            stateMachineArn=arn,
            input=json.dumps(payload),
        )
        logger.debug(f"Step Machine response is: {response}")
        return response
