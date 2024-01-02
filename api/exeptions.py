from .models.base_model import BaseModel

from typing import final


class ApiError(Exception, BaseModel):
    _code: int | None = None
    _message: str | None = None

    def __init__(self, message: str | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

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