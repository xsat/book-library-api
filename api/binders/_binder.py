from flask import Request

from typing import final


class Binder:
    @final
    def __init__(self, request: Request) -> None:
        self._assign(request)

    def _assign(self, request: Request) -> None:
        raise NotImplementedError
