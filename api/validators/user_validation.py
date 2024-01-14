from ._validation import Validation
from ..binders.login_binder import LoginBinder


class UserValidation(Validation):
    __error_message: str

    def __init__(self, login_binder: LoginBinder) -> None:
        self.__login_binder = login_binder

    def is_valid(self) -> bool:
        if not self._is_length_valid(self.__login_binder.username):
            self.__error_message = "invalid_username"
            return False

        if not self._is_length_valid(self.__login_binder.password):
            self.__error_message = "invalid_password"
            return False

        return True

    def error_message(self) -> str:
        return self.__error_message
