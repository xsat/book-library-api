from flask import Blueprint, request

from ..auth import AuthorizedUser, authorize_user
from ..binders.user_binder import UserBinder
from ..exeptions import BadRequestError
from ..mappers.user_tokens_mapper import user_token_create_by_user
from ..mappers.users_mapper import (
    user_create_by_binder,
    user_delete,
    user_update_by_binder,
)
from ..models.user import User
from ..models.user_token import UserToken
from ..validators.user_validation import UserValidation

user_controller: Blueprint = Blueprint("user_controller", __name__, url_prefix="/user")


@user_controller.route("/", methods=["POST"])
def user_create() -> dict[str, User | UserToken]:
    user_binder: UserBinder = UserBinder(request)
    user_validation: UserValidation = UserValidation(user_binder)
    if not user_validation.is_valid():
        raise BadRequestError(user_validation.error_message())

    user: User = user_create_by_binder(user_binder)
    user_token: UserToken = user_token_create_by_user(user)

    return {
        "user": user,
        "user_token": user_token,
    }


@user_controller.route("/", methods=["GET"])
@authorize_user
def user_get(authorized_user: AuthorizedUser) -> dict[str, User]:
    return {
        "user": authorized_user.user,
    }


@user_controller.route("/", methods=["PUT"])
@authorize_user
def user_update(authorized_user: AuthorizedUser) -> dict[str, User]:
    user_binder: UserBinder = UserBinder(request)
    user_validation: UserValidation = UserValidation(user_binder, authorized_user.user)
    if not user_validation.is_valid():
        raise BadRequestError(user_validation.error_message())

    user_update_by_binder(authorized_user.user, user_binder)

    return {
        "user": authorized_user.user,
    }


@user_controller.route("/", methods=["DELETE"])
@authorize_user
def users_user_delete(authorized_user: AuthorizedUser) -> dict[str, None]:
    user_delete(authorized_user.user)

    return {
        "user": None,
    }
