from flask import Request
from typing import final, Any


def _prepare_value(value: Any) -> Any:
    if isinstance(value, str):
        return value.strip()

    return value


class Binder:
    @final
    def __init__(self, request: Request) -> None:
        values: dict = request.values.to_dict()
        json: Any = request.get_json(silent=True)
        if isinstance(json, dict):
            values.update(json)

        for key, value in values.items():
            values[key] = _prepare_value(value)

        self._assign(values)

    def _assign(self, values: dict) -> None:
        raise NotImplementedError
