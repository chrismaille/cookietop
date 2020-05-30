from random import choice
from typing import Any, Dict

from aws_lambda_context import LambdaContext
from loguru import logger

from interface.aws.handler_step_function import handler_step


@handler_step()
def find_step(event: Dict[Any, Any], context: LambdaContext) -> Dict[Any, Any]:
    """Create {{cookiecutter.domain_class}} step.

    This is part 1 from Create {{ cookiecutter.domain_class }} State Machine
    Current Step: Find instance

    To understand this flow, please
    check on CloudWatch the following logs.

    The return dict will be used on
    "{{cookiecutter.domain}} exists?" Step.

    """
    logger.debug("Start step 1: Find {{cookiecutter.domain_class}}")
    logger.debug(f"Event received: {event}")
    return {"exists": choice([True, False])}
