from flask import Blueprint

from ..auth import authorize_user, AuthorizedUser


books_controller: Blueprint = Blueprint("books_controller", __name__, url_prefix="/books")


@books_controller.route("/", methods=["GET"])
@authorize_user
def books_list_get(authorized_user: AuthorizedUser) -> dict:
    return {
        "list": []
    }


@books_controller.route("/", methods=["POST"])
@authorize_user
def books_list_post(authorized_user: AuthorizedUser) -> dict:
    return {
        "book_id": 1
    }


@books_controller.route("/<int:book_id>", methods=["GET"])
@authorize_user
def books_item_get(book_id: int, authorized_user: AuthorizedUser) -> dict:
    return {
        "book_id": book_id
    }


@books_controller.route("/<int:book_id>", methods=["PUT"])
@authorize_user
def books_item_put(book_id: int, authorized_user: AuthorizedUser) -> dict:
    return {
        "book_id": book_id
    }


@books_controller.route("/<int:book_id>", methods=["DELETE"])
@authorize_user
def books_item_delete(book_id: int, authorized_user: AuthorizedUser) -> dict:
    return {
        "book_id": book_id
    }
