from datetime import datetime
from typing import Union

import arrow


def get_time_now(as_string: bool = False) -> Union[str, datetime]:
    """Return current time.

    To freeze time in Factory
    wrap them using `freeze_time` decorator

    :return: datetime object
    """
    now = arrow.utcnow()
    return now.iso_format() if as_string else now.datetime
