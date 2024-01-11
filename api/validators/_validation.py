from typing import final


class Validation:
    def is_valid(self) -> bool:
        raise NotImplementedError

    def error_message(self) -> str:
        raise NotImplementedError

    @final
    def _is_length_valid(self, value: str, min_length: int = 1, max_length: int = 255) -> bool:
        value_length: int = len(value)
        if value_length < min_length or value_length > max_length:
            return False

        return True

    @final
    def _is_numeric_valid(self, value: int, min_value: int = 0, max_value: int = 999_999) -> bool:
        if value < min_value or value > max_value:
            return False

        return True
