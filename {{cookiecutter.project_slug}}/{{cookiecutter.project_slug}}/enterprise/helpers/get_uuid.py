from typing import Union
from uuid import uuid4, UUID


def get_uuid(string: bool = False) -> Union[str, UUID]:
    """Return UUID4 string.

    :type string: Return as string
    :return: String
    """
    return str(uuid4()) if string else uuid4()
