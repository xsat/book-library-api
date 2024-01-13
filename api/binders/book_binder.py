from ._binder import Binder


class BookBinder(Binder):
    def _assign(self, values: dict) -> None:
        self.__title = values.get("title")
        self.__pages = values.get("pages")

    @property
    def title(self) -> str:
        if self.__title is None:
            return ""

        return str(self.__title)

    @property
    def pages(self) -> int:
        if self.__pages is None:
            return 0

        return int(self.__pages)
