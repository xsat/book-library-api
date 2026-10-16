from typing import Any, final

from .json import JsonSerializable


class ApiError(Exception, JsonSerializable):
    _code: int = 0
    _message: str | None = None

    def __init__(self, message: str | None = None, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

        if message is not None:
            self._message = message

    @final
    @property
    def code(self) -> int:
        return self._code

    @final
    def json_serialize(self) -> dict[str, int | str | None]:
        return {
            "code": self._code,
            "message": self._message,
        }


class BadRequestError(ApiError):
    _code: int = 400


class UnauthorizedError(ApiError):
    _code: int = 401
    _message: str | None = "unauthorized"


class NotFoundError(ApiError):
    _code: int = 404
    _message: str | None = "not_found"


class InternalServerError(ApiError):
    _code: int = 500
    