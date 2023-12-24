from flask import Blueprint
from flask import request


from ..data_mappers.users_data_mapper import user_find_by_username
from ..password import password_check


auth_controller: Blueprint = Blueprint('auth_controller', __name__, url_prefix='/auth')


@auth_controller.route("/", methods=["POST"])
def auth_login() -> dict:
    username: str | None = request.json.get('username')
    password: str | None = request.json.get('password')
    error: str | None = None

    found_user = user_find_by_username(username)
    if found_user is None or not password_check(password, found_user['password_hash']):
        error = "Username or password are invalid"
        found_user = None

    return {
        "error": error,
        "found_user": found_user,
        "debug": {
            "username": username,
            "password": password
        },
        "access_token": None
    }


@auth_controller.route("/", methods=["DELETE"])
def auth_logout() -> dict:
    return {}
