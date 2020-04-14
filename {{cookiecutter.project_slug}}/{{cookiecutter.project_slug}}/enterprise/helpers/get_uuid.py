from uuid import uuid4


def get_uuid() -> str:
    """Return UUID4 string.

    :return: String
    """
    return uuid4().hex
