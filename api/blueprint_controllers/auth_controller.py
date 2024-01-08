from flask import Blueprint, request

from ..auth import authorize_user, AuthorizedUser
from ..exeptions import BadRequestError

from ..models.user import User
from ..models.user_token import UserToken
from ..binders.login_binder import LoginBinder
from ..validators.login_validation import LoginValidation
from ..mappers.user_tokens_mapper import user_token_create_by_user, user_token_delete_by_authorized_user


auth_controller: Blueprint = Blueprint("auth_controller", __name__, url_prefix="/auth")


@auth_controller.route("/", methods=["POST"])
def auth_login() -> dict:
    login_binder: LoginBinder = LoginBinder(request)
    bind_user: User = User(0, "", "")
    login_validation: LoginValidation = LoginValidation(login_binder, bind_user)
    if not login_validation.is_valid():
        raise BadRequestError(login_validation.error_message())

    user_token: UserToken = user_token_create_by_user(bind_user)

    return {
        "user_token": user_token,
    }


@auth_controller.route("/", methods=["DELETE"])
@authorize_user
def auth_logout(authorized_user: AuthorizedUser) -> dict:
    user_token_delete_by_authorized_user(authorized_user)

    return {
        "user_token": None,
    }
