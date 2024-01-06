from flask import Request
from typing import Any

from ._binder import Binder


class LoginBinder(Binder):
    __username: Any
    __password: Any

    def _assign(self, request: Request) -> None:
        self.__username = request.json.get("username")
        self.__password = request.json.get("password")

    def username(self) -> Any:
        return self.__username

    def password(self) -> Any:
        return self.__password
