from flask.json.provider import DefaultJSONProvider
from typing import Any, Callable

from .models.base_model import BaseModel


def _default(o: Any) -> Any:
    if isinstance(o, BaseModel):
        return o.json_serialize()

    return DefaultJSONProvider.default(o)


class ModelJSONProvider(DefaultJSONProvider):
    default: Callable[[Any], Any] = staticmethod(_default)
