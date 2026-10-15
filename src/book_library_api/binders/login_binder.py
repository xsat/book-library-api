from ._binder import Binder


class LoginBinder(Binder):
    def _assign(self, values: dict) -> None:
        self.__username = values.get("username")
        self.__password = values.get("password")

    @property
    def username(self) -> str:
        if self.__username is None:
            return ""

        return str(self.__username)

    @property
    def password(self) -> str:
        if self.__password is None:
            return ""

        return str(self.__password)
