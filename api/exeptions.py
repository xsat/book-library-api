from .json import JsonSerializable

from typing import final


class ApiError(Exception, JsonSerializable):
    _code: int | None = None
    _message: str | None = None

    def __init__(self, message: str | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if message is not None:
            self._message = message

    @final
    @property
    def code(self) -> int:
        return self._code

    @final
    def json_serialize(self) -> dict:
        return {
            "code": self._code,
            "message": self._message,
        }


class BadRequestError(ApiError):
    _code: int = 400


class UnauthorizedError(ApiError):
    _code: int = 401
    _message: str = "unauthorized"


class NotFoundError(ApiError):
    _code: int = 404
    _message: str = "not_found"
