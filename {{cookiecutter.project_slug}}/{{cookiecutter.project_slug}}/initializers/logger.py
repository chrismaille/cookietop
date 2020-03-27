import logging

from loguru import logger
from pythonjsonlogger import jsonlogger
from stela import settings


def initialize_logger():
    logger.info(f"Initializing Logger...")
    if settings["logger.use_json_format"]:
        log_handler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(lineno)d - %(message)s'
        )
        log_handler.setFormatter(formatter)
        config = {
            "handlers": [
                {"sink": log_handler, "format": "{message}", "serialize": True,},
            ],
        }
        logger.configure(**config)
