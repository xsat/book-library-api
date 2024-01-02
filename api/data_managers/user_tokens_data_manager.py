from ..models.user import User
from ..models.user_token import UserToken
from ..hash import access_token_generate
from ..db import execute
from ..datetime import today_datetime, next_month_datetime, to_mysql_datetime

from datetime import datetime


def user_token_create_by_user(user: User) -> UserToken:
    access_token: str = access_token_generate()
    created_at: datetime = today_datetime()
    expired_at: datetime = next_month_datetime()
    user_token_id: int | None = execute(
        "INSERT INTO `user_tokens` (`user_id`, `access_token`, `created_at`, `expired_at`) " +
        "VALUE (%s, %s, %s, %s)",
        (user.user_id(), access_token, to_mysql_datetime(created_at), to_mysql_datetime(expired_at))
    )

    return UserToken(user_token_id, user.user_id(), access_token, created_at, expired_at)
