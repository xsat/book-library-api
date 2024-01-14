from ..db import query_one, execute
from ..hash import password_generate
from ..datetime import today_datetime, to_mysql_datetime
from ..models.user import User
from ..binders.user_binder import UserBinder


def user_find_by_username(username: str) -> User | None:
    result: dict | None = query_one(
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
    result: dict | None = query_one(
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


def user_create_by_binder(user_binder: UserBinder) -> User:
    password_hash: str = password_generate(user_binder.password)
    user_id: int | None = execute(
        "INSERT INTO `users` (`username`, `password_hash`) " +
        "VALUE (%s, %s)",
        (user_binder.username, password_hash)
    )

    return User(user_id, user_binder.username, password_hash)


def user_update_by_binder(user: User, user_binder: UserBinder) -> None:
    password_hash: str = password_generate(user_binder.password)
    updated_user: User = User(user.user_id, user_binder.username, password_hash)
    user.assign(updated_user)

    execute(
        "UPDATE `users` AS u " +
        "SET u.`username` = %s, u.`password_hash` = %s " +
        "WHERE u.`user_id` = %s",
        (user.username, password_hash, user.user_id)
    )


def user_delete(user: User) -> None:
    execute(
        "DELETE FROM `users` AS u " +
        "WHERE u.`user_id` = %s",
        (user.user_id, )
    )


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
