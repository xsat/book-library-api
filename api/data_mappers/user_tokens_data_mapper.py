from ..models.user_token import UserToken
from ..db import execute


def user_token_create(user_token: UserToken) -> bool:
    user_token_id: int | None = execute(
        "INSERT INTO `user_tokens` (`user_id`, `access_token`, `created_at`, `expired_at`) " +
        "VALUE (%d, %s, %s, %s)",
        (user_token["user_id"], user_token["access_token"], user_token['created_at'], user_token['expired_at'])
    )
    user_token["user_token_id"] = user_token_id

    return user_token is not None
