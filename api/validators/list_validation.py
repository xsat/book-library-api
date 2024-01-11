from ._validation import Validation
from ..binders.list_binder import ListBinder, ORDER_ALLOWED_VALUES, SORT_ALLOWED_VALUES


class ListValidation(Validation):
    __error_message: str

    def __init__(self, list_binder: ListBinder) -> None:
        self.__list_binder = list_binder

    def is_valid(self) -> bool:
        if not self._is_numeric_valid(self.__list_binder.offset):
            self.__error_message = "invalid_offset"

            return False

        if not self._is_numeric_valid(self.__list_binder.limit):
            self.__error_message = "invalid_limit"

            return False

        if self.__list_binder.order not in ORDER_ALLOWED_VALUES:
            self.__error_message = "invalid_order"

            return False

        if self.__list_binder.sort not in SORT_ALLOWED_VALUES:
            self.__error_message = "invalid_sort"

            return False

        if not self._is_length_valid(self.__list_binder.search, min_length=0):
            self.__error_message = "invalid_search"

            return False

        return True

    def error_message(self) -> str:
        return self.__error_message
