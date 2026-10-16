from ..binders.author_binder import AuthorBinder
from ._validation import Validation


class AuthorValidation(Validation):
    def __init__(self, author_binder: AuthorBinder) -> None:
        self.__author_binder = author_binder

    def is_valid(self) -> bool:
        return self._is_length_valid(self.__author_binder.name)

    def error_message(self) -> str:
        return "invalid_name"
