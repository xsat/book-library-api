from ._validation import Validation

from ..binders.list_binder import ListBinder


class ListValidation(Validation):
    def __init__(self, list_binder: ListBinder) -> None:
        self.__list_binder = list_binder

    def is_valid(self) -> bool:
        if not self._is_length_valid(self.__list_binder.search, min_length=0):
            return False

        return True

    def error_message(self) -> str:
        return "Search is invalid"
