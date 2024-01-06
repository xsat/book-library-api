from ..models.user import User
from ..db import query_one

from ..datetime import today_datetime, to_mysql_datetime


def user_find_by_username(username: str) -> User | None:
    result = query_one(
        "SELECT u.`user_id`, u.`username`, u.`password_hash` " +
        "FROM `users` AS u " +
        "WHERE u.`username` = %s " +
        "LIMIT 1",
        (username, )
    )

    if result is not None:
        return _build_user_from_dict(result)

    return None


def user_find_by_valid_access_token(access_token: str) -> User | None:
    result = query_one(
        "SELECT u.`user_id`, u.`username`, u.`password_hash` " +
        "FROM `users` AS u "
        "INNER JOIN `user_tokens` AS ut " +
        "ON ut.`user_id` = u.`user_id` AND ut.`access_token` = %s AND ut.`expired_at` >= %s" +
        "LIMIT 1",
        (access_token, to_mysql_datetime(today_datetime()))
    )

    if result is not None:
        return _build_user_from_dict(result)

    return None


def _build_user_from_dict(data: dict) -> User:
    if ("user_id" not in data
            or "username" not in data
            or "password_hash" not in data):
        raise ValueError(data)

    return User(
        data["user_id"],
        data["username"],
        data["password_hash"]
    )
