from typing import Any

from ._binder import Binder


class AuthorBinder(Binder):
    def _assign(self, json: dict) -> None:
        self.__name = json.get("name")

    @property
    def name(self) -> Any:
        return self.__name
