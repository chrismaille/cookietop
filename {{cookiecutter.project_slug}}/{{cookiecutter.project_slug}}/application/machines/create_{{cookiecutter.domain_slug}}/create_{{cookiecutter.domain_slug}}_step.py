from loguru import logger


def create_step(event, context):
    """Create {{cookiecutter.domain_class}} step.

    This is part from Create {{ cookiecutter.domain_class }} State Machine
    Current Step: Create

    """
    logger.debug("Start step: Create {{cookiecutter.domain_class}}")
