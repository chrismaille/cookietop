from typing import Any, Dict

from aws_lambda_context import LambdaContext
from loguru import logger

from interface.aws.handler_step_function import step


@step()
def find_step(event: Dict[Any, Any], context: LambdaContext) -> Dict[Any, Any]:
    """Find {{cookiecutter.model_name_camel}} step."""
    logger.debug("Start step: Find {{cookiecutter.model_name_camel}}")
    logger.debug(f"Event received: {event}")
    return {"success": True}
