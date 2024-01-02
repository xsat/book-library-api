from ..models.user import User, build_user_from_dict
from ..db import select_one


def user_find_by_username(username: str) -> User | None:
    result = select_one(
        "SELECT u.`user_id`, u.`username`, u.`password_hash` " +
        "FROM `users` AS u " +
        "WHERE u.`username` = %s " +
        "LIMIT 1",
        (username, )
    )

    if result is not None:
        return build_user_from_dict(result)

    return None


def user_find_by_access_token(access_token: str) -> User | None:
    result = select_one(
        "SELECT u.`user_id`, u.`username`, u.`password_hash` " +
        "FROM `users` AS u "
        "INNER JOIN `user_tokens` AS ut " +
        "ON ut.`user_id` = u.`user_id` AND ut.`access_token` = %s " +
        "LIMIT 1",
        (access_token, )
    )

    if result is not None:
        return build_user_from_dict(result)

    return None
