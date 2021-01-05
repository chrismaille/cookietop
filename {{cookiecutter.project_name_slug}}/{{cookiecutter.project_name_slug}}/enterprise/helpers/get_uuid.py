from typing import Union
from uuid import uuid4, UUID


def get_uuid(as_string: bool = False) -> Union[str, UUID]:
    """Return UUID4 string.

    :type as_string: Return as string
    :return: String
    """
    return str(uuid4()) if as_string else uuid4()
