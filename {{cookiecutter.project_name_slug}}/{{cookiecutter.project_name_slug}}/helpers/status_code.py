from enum import unique, Enum


@unique
class StatusCode(Enum):
    """HTTP Requests Status Code."""

    OK = 200
    CREATED = 201
    DELETED = 204
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_ERROR = 500
