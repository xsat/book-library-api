from ._binder import Binder


class ListBinder(Binder):
    def _assign(self, values: dict) -> None:
        self.__offset = values.get("offset", 0)
        self.__limit = values.get("limit", 10)

    @property
    def offset(self) -> int:
        if self.__offset is None:
            return 0

        return int(self.__offset)

    @property
    def limit(self) -> int:
        if self.__limit is None:
            return 0

        return int(self.__limit)
