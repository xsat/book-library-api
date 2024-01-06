from flask import Request

from typing import final, Any


class Binder:
    @final
    def __init__(self, request: Request) -> None:
        json: Any = request.get_json(silent=True)
        if isinstance(json, dict):
            self._assign(json)
        else:
            self._assign({})

    def _assign(self, json: dict) -> None:
        raise NotImplementedError
