from ._binder import Binder


class AuthorBinder(Binder):
    def _assign(self, values: dict) -> None:
        self.__name = values.get("name")

    @property
    def name(self) -> str:
        if self.__name is None:
            return ""

        return str(self.__name)
