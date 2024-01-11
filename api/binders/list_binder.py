from ._binder import Binder


_SORT_DESC: str = "desc"
_SORT_ASC: str = "asc"

_ORDER_CREATED_AT: str = "created_at"

SORT_ALLOWED_VALUES: list[str] = [_SORT_DESC, _SORT_ASC]
ORDER_ALLOWED_VALUES: list[str] = [_ORDER_CREATED_AT]


class ListBinder(Binder):
    def _assign(self, values: dict) -> None:
        self.__offset = values.get("offset", 0)
        self.__limit = values.get("limit", 10)
        self.__sort = values.get("sort", _SORT_DESC)
        self.__order = values.get("order", _ORDER_CREATED_AT)
        self.__search = values.get("search")

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

    @property
    def sort(self) -> str:
        if self.__sort is None:
            return ""

        return str(self.__sort)

    @property
    def order(self) -> str:
        if self.__order is None:
            return ""

        return str(self.__order)

    @property
    def search(self) -> str:
        if self.__search is None:
            return ""

        return str(self.__search)
