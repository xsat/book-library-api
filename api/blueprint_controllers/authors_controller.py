from flask import Blueprint

from ..auth import authorize_user, AuthorizedUser


authors_controller: Blueprint = Blueprint("authors_controller", __name__, url_prefix="/authors")


@authors_controller.route("/", methods=["GET"])
@authorize_user
def authors_list_get(authorized_user: AuthorizedUser) -> dict:
    return {
        "list": []
    }


@authors_controller.route("/", methods=["POST"])
@authorize_user
def authors_list_post(authorized_user: AuthorizedUser) -> dict:
    return {
        "book_id": 1
    }


@authors_controller.route("/<int:author_id>", methods=["GET"])
@authorize_user
def authors_item_get(author_id: int, authorized_user: AuthorizedUser) -> dict:
    return {
        "author_id": author_id
    }


@authors_controller.route("/<int:author_id>", methods=["PUT"])
@authorize_user
def authors_item_put(author_id: int, authorized_user: AuthorizedUser) -> dict:
    return {
        "author_id": author_id
    }


@authors_controller.route("/<int:author_id>", methods=["DELETE"])
@authorize_user
def authors_item_delete(author_id: int, authorized_user: AuthorizedUser) -> dict:
    return {
        "author_id": author_id
    }
