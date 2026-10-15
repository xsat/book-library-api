from collections.abc import Callable
from typing import Any

from flask.json.provider import DefaultJSONProvider


def _default(o: Any) -> Any:
    if isinstance(o, JsonSerializable):
        return o.json_serialize()

    return DefaultJSONProvider.default(o)


class ModelJSONProvider(DefaultJSONProvider):
    default: Callable[[Any], Any] = staticmethod(_default)
    sort_keys = False


class JsonSerializable:
    def json_serialize(self) -> dict[Any, Any]:
        raise NotImplementedError
