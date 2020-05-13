from pathlib import Path

import toml
from loguru import logger
from scalpl import Cut
from sentry_sdk.utils import BadDsn
from stela import settings
import sentry_sdk as sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration


def initialize_sentry() -> None:
    """Initialize Sentry monitoring.

    To enable Sentry, please define
    settings "sentry.endpoint" or
    environment SENTRY_ENDPOINT.

    """
    endpoint = settings["sentry.endpoint"]
    if not endpoint:
        logger.warning("Sentry not initialized.")
        return

    toml_path = Path().cwd().joinpath("pyproject.toml")
    with open(str(toml_path), "r") as file:
        data = Cut(toml.load(file))
        current_version = data["tool.poetry.version"]

    try:
        sentry_sdk.init(
            dsn=endpoint,
            integrations=[AwsLambdaIntegration()],
            environment=settings.stela_options.current_environment,
            release=current_version,
        )
        logger.info("Sentry initialized.")
    except BadDsn as error:
        logger.error(f"Error when initializing Sentry: {error}")
