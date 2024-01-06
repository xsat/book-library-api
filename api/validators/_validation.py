class Validation:
    def is_valid(self) -> bool:
        raise NotImplementedError

    def error_message(self) -> str:
        raise NotImplementedError
