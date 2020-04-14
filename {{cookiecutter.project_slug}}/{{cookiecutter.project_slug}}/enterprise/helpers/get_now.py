from datetime import datetime

import arrow


def get_now() -> datetime:
    """Return current time.

    To freeze time in Factory
    wrap them using `freeze_time` decorator

    :return: datetime object
    """
    return arrow.utcnow().datetime  # type: ignore
