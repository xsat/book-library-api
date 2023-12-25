from ..models.user import User
from ..models.user_token import UserToken
from ..hash import access_token_generate
from ..db import execute

from datetime import datetime


DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"


def user_token_create_by_user(user: User) -> UserToken:
    access_token: str = access_token_generate()
    created_at: datetime = datetime.now()
    expired_at: datetime = datetime.now()

    if expired_at.month == 12:
        expired_at.replace(year=expired_at.year + 1, month=1)
    else:
        expired_at.replace(month=expired_at.month + 1)

    user_token_id: int | None = execute(
        "INSERT INTO `user_tokens` (`user_id`, `access_token`, `created_at`, `expired_at`) " +
        "VALUE (%s, %s, %s, %s)",
        (user.user_id(), access_token, created_at.strftime(DATETIME_FORMAT), expired_at.strftime(DATETIME_FORMAT))
    )

    return UserToken(user_token_id, user.user_id(), access_token, created_at, expired_at)
