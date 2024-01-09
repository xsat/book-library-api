from ._validation import Validation

from ..binders.author_binder import AuthorBinder


class AuthorValidation(Validation):
    def __init__(self, author_binder: AuthorBinder) -> None:
        self.__author_binder = author_binder

    def is_valid(self) -> bool:
        if not self._is_length_valid(self.__author_binder.name):
            return False

        return True

    def error_message(self) -> str:
        return "Name is invalid"
