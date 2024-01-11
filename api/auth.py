from flask import request
from functools import wraps
from typing import Callable, Any

from .exeptions import UnauthorizedError
from .models.user import User
from .mappers.users_mapper import user_find_by_valid_access_token


class AuthorizedUser:
    def __init__(self, user: User, access_token: str) -> None:
        self.__user = user
        self.__access_token = access_token

    @property
    def user(self) -> User:
        return self.__user

    @property
    def access_token(self) -> str:
        return self.__access_token


def authorize_user(func: Callable) -> Callable:
    @wraps(func)
    def decorator(*args, **kwargs) -> Any:
        kwargs["authorized_user"] = _find_authorized_user()
        return func(*args, **kwargs)

    return decorator


def _find_authorized_user() -> AuthorizedUser:
    value: Any = request.headers.get("Authorization")
    if not isinstance(value, str):
        raise UnauthorizedError()

    scheme, _, access_token = value.partition(" ")
    if scheme != "Bearer":
        raise UnauthorizedError()

    found_user: User | None = user_find_by_valid_access_token(access_token)
    if found_user is None:
        raise UnauthorizedError()

    return AuthorizedUser(found_user, access_token)
