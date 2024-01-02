from flask.json.provider import DefaultJSONProvider
from typing import Any, Callable


def _default(o: Any) -> Any:
    if isinstance(o, JsonSerializable):
        return o.json_serialize()

    return DefaultJSONProvider.default(o)


class ModelJSONProvider(DefaultJSONProvider):
    default: Callable[[Any], Any] = staticmethod(_default)


class JsonSerializable:
    def json_serialize(self) -> dict:
        raise NotImplementedError
