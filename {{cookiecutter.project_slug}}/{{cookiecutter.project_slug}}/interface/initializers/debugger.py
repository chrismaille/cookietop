import os
from loguru import logger

def initialize_debug() -> None:
    if  os.getenv("DEBUG", "false").lower() == 'true':
        import ptvsd
        logger.info('-------------------------------------------------> WAITING CONNECTION ON 0.0.0.0:5890 TO DEBUG ')
        ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
        ptvsd.wait_for_attach()
