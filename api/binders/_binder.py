from flask import Request

from typing import final, Any


def _prepare_value(value: Any) -> Any:
    if isinstance(value, str):
        return value.strip()

    return value


class Binder:
    @final
    def __init__(self, request: Request) -> None:
        json: Any = request.get_json(silent=True)
        if isinstance(json, dict):
            for key, value in json.items():
                json[key] = _prepare_value(value)

            self._assign(json)
        else:
            self._assign({})

    def _assign(self, json: dict) -> None:
        raise NotImplementedError
