from loguru import logger


def find_step(event, context):
    """Create {{cookiecutter.domain_class}} step.

    This is part from Create {{ cookiecutter.domain_class }} State Machine
    Current Step: Find

    """
    logger.debug("Start step: Find {{cookiecutter.domain_class}}")
