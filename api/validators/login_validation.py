from ._validation import Validation

from ..binders.login_binder import LoginBinder
from ..mappers.users_mapper import user_find_by_username
from ..hash import password_check

from ..models.user import User


class LoginValidation(Validation):
    def __init__(self, login_binder: LoginBinder, bind_user: User) -> None:
        self.__login_binder = login_binder
        self.__bind_user = bind_user

    def is_valid(self) -> bool:
        if not self._is_length_valid(self.__login_binder.username):
            return False

        if not self._is_length_valid(self.__login_binder.password):
            return False

        found_user = user_find_by_username(self.__login_binder.username)
        if found_user is None or not password_check(self.__login_binder.password, found_user.password_hash):
            return False

        self.__bind_user.assign(found_user)

        return True

    def error_message(self) -> str:
        return "Username or password are invalid"
