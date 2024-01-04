from .data_managers.users_data_manager import user_find_by_access_token

from .models.user import User
from .exeptions import UnauthorizedError

from functools import wraps
from typing import Callable, Any
from flask import request


class AuthorizedUser:
    __user: User
    __access_token: str

    def __init__(self, user: User, access_token: str) -> None:
        self.__user = user
        self.__access_token = access_token

    def user(self) -> User:
        return self.__user

    def access_token(self) -> str:
        return self.__access_token


def authorize_user(func: Callable) -> Callable:
    @wraps(func)
    def decorator(*args, **kwargs) -> Any:
        kwargs["authorized_user"] = _get_authorized_user()
        return func(*args, **kwargs)

    return decorator


def _get_authorized_user() -> AuthorizedUser:
    value: Any = request.headers.get("Authorization")
    if not isinstance(value, str):
        raise UnauthorizedError("Unauthorized")

    scheme, _, access_token = value.partition(" ")

    if scheme != "Bearer":
        raise UnauthorizedError("Unauthorized")

    found_user: User | None = user_find_by_access_token(access_token)
    if found_user is None:
        raise UnauthorizedError("Unauthorized")

    return AuthorizedUser(found_user, access_token)
