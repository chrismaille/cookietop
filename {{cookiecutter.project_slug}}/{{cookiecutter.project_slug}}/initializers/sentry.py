import pkg_resources
from loguru import logger
from stela import settings
import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration


def initialize_sentry():
    """
    Function that initialize Sentry monitoring
    """
    if not settings["sentry.endpoint"]:
        logger.warning(f"Sentry not initialized.")
        return

    current_version = pkg_resources.get_distribution(
        '{{cookiecutter.project_slug}}'
    ).version

    sentry_sdk.init(
        dsn=settings["sentry.endpoint"],
        integrations=[AwsLambdaIntegration()],
        environment=settings.stela_options.current_environment,
        release=current_version,
    )
    logger.info(f"Sentry initialized.")
