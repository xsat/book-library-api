from typing import Any

from ._binder import Binder


class LoginBinder(Binder):
    def _assign(self, json: dict) -> None:
        self.__username = json.get("username")
        self.__password = json.get("password")

    @property
    def username(self) -> Any:
        return self.__username

    @property
    def password(self) -> Any:
        return self.__password
