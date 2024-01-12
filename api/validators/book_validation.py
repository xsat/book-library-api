from ._validation import Validation
from ..binders.book_binder import BookBinder


class BookValidation(Validation):
    __error_message: str

    def __init__(self, book_binder: BookBinder) -> None:
        self.__book_binder = book_binder

    def is_valid(self) -> bool:
        if not self._is_length_valid(self.__book_binder.title):
            self.__error_message = "invalid_title"

            return False

        if not self._is_numeric_valid(self.__book_binder.pages):
            self.__error_message = "invalid_pages"

            return False

        return True

    def error_message(self) -> str:
        return self.__error_message
