from typing import Any

from flask import Blueprint
from flask import request

from ..exeptions import BadRequestError

from ..data_managers.users_data_manager import user_find_by_username
from ..data_managers.user_tokens_data_manager import user_token_create_by_user
from ..hash import password_check
from ..models.user_token import UserToken


auth_controller: Blueprint = Blueprint('auth_controller', __name__, url_prefix='/auth')


@auth_controller.route("/", methods=["POST"])
def auth_login() -> dict:
    username: Any = request.json.get('username')
    password: Any = request.json.get('password')

    if not isinstance(username, str):
        raise BadRequestError("Username or password are invalid")

    found_user = user_find_by_username(username)
    if found_user is None or not password_check(password, found_user.password_hash()):
        raise BadRequestError("Username or password are invalid")

    user_token: UserToken = user_token_create_by_user(found_user)

    return {
        "user_token": user_token
    }


@auth_controller.route("/", methods=["DELETE"])
def auth_logout() -> dict:
    return {}
