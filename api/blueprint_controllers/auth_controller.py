from typing import Any

from flask import Blueprint
from flask import request

from werkzeug.exceptions import UnsupportedMediaType

from ..exeptions import BadRequestError

from ..mappers.users_mapper import user_find_by_username
from ..mappers.user_tokens_mapper import user_token_create_by_user, user_token_delete_by_authorized_user
from ..hash import password_check
from ..models.user_token import UserToken

from ..auth import authorize_user, AuthorizedUser


auth_controller: Blueprint = Blueprint("auth_controller", __name__, url_prefix="/auth")


@auth_controller.route("/", methods=["POST"])
def auth_login() -> dict:
    try:
        username: Any = request.json.get("username")
        password: Any = request.json.get("password")
    except UnsupportedMediaType:
        raise BadRequestError("Username or password are invalid")

    if not isinstance(username, str):
        raise BadRequestError("Username or password are invalid")

    found_user = user_find_by_username(username)
    if found_user is None or not password_check(password, found_user.password_hash()):
        raise BadRequestError("Username or password are invalid")

    user_token: UserToken = user_token_create_by_user(found_user)

    return {
        "user_token": user_token,
    }


@auth_controller.route("/", methods=["DELETE"])
@authorize_user
def auth_logout(authorized_user: AuthorizedUser) -> dict:
    user_token_delete_by_authorized_user(authorized_user)

    return {}
