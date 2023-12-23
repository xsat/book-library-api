from flask import Blueprint
from flask import request
from hashlib import md5


from ..data_mappers.users_data_mapper import user_find_by_username


auth_controller: Blueprint = Blueprint('auth_controller', __name__, url_prefix='/auth')


@auth_controller.route("/", methods=["POST"])
def auth_login() -> dict:
    username: str | None = request.json.get('username')
    password: str | None = request.json.get('password')

    md5(bytes(password)).hexdigest()

    found_user = user_find_by_username(username)

    if found_user is not None and md5(password).hexdigest() == found_user['password_hash']:
        md5(password).hexdigest()


    return {
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
