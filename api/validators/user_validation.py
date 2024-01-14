from ._validation import Validation
from ..models.user import User
from ..binders.user_binder import UserBinder
from ..mappers.users_mapper import user_find_by_username


class UserValidation(Validation):
    __error_message: str

    def __init__(self, user_binder: UserBinder, user: User | None = None) -> None:
        self.__user_binder = user_binder
        self.__user = user

    def is_valid(self) -> bool:
        if not self._is_length_valid(self.__user_binder.username):
            self.__error_message = "invalid_username"
            return False

        if not self._is_length_valid(self.__user_binder.password):
            self.__error_message = "invalid_password"
            return False

        found_user: User | None = user_find_by_username(self.__user_binder.username)
        if found_user is not None:
            if self.__user is not None and found_user.user_id != self.__user.user_id:
                self.__error_message = "invalid_username"
                return False
            elif self.__user is None:
                self.__error_message = "invalid_username"
                return False

        return True

    def error_message(self) -> str:
        return self.__error_message
