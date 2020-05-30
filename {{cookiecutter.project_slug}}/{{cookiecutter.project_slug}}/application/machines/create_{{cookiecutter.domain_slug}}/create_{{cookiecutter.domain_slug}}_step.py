from typing import Any, Dict

from aws_lambda_context import LambdaContext
from loguru import logger

from interface.aws.handler_step_function import handler_step


@handler_step()
def create_step(event: Dict[Any, Any], context: LambdaContext) -> Dict[Any, Any]:
    """Create {{cookiecutter.domain_class}} step.

    This is part 2a from Create {{ cookiecutter.domain_class }} State Machine
    Current Step: Create

    """
    logger.debug("Start step 2a: Create {{cookiecutter.domain_class}}")
    logger.debug(f"Event received: {event}")
    return {"result": "foo"}
