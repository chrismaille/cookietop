import pkg_resources
from loguru import logger
from stela import settings
import sentry_sdk as sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration


def initialize_sentry() -> None:
    """Initialize Sentry monitoring.

    To enable Sentry, please define
    settings "sentry.endpoint" or
    environment SENTRY_ENDPOINT.

    """
    if not settings["sentry.endpoint"]:
        logger.warning(f"Sentry not initialized.")
        return

    # fmt: off
    current_version = pkg_resources.get_distribution(
        '{{cookiecutter.project_slug}}'
    ).version
    # fmt: on

    sentry_sdk.init(
        dsn=settings["sentry.endpoint"],
        integrations=[AwsLambdaIntegration()],
        environment=settings.stela_options.current_environment,
        release=current_version,
    )
    logger.info(f"Sentry initialized.")
