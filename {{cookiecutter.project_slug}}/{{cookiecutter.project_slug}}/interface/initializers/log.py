import logging

from loguru import logger
from pythonjsonlogger import jsonlogger
from stela import settings


def initialize_log() -> None:
    """Initialize application logs.

    More info: https://github.com/Delgan/loguru

    If the settings "logger.use_json_format"
    or LOGGER_USE_JSON_FORMAT environment is True
    all logging will be converted to JSON format.

    Otherwise format will be Loguru standard.

    """
    logger.info(f"Initializing Logger...")
    if settings["logger.use_json_format"]:
        log_handler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(lineno)d - %(message)s"
        )
        log_handler.setFormatter(formatter)
        config = {
            "handlers": [
                {
                    "sink": log_handler,
                    "format": "{message}",
                    "serialize": True,
                    "level": settings["logger.level"],
                },
            ],
        }
        logger.configure(**config)  # type: ignore
