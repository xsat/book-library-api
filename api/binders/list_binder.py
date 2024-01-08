from typing import Any

from ._binder import Binder


class ListBinder(Binder):
    def _assign(self, json: dict) -> None:
        self.__offset = json.get("offset", 0)
        self.__limit = json.get("limit", 10)

    @property
    def offset(self) -> Any:
        return self.__offset

    @property
    def limit(self) -> Any:
        return self.__limit