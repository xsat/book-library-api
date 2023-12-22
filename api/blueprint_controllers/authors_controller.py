from flask import Blueprint
from ..models.author import Author
from ..db import select_one, select_all


authors_controller: Blueprint = Blueprint('authors_controller', __name__, url_prefix='/authors')


@authors_controller.route("/", methods=["GET"])
def authors_list_get() -> dict:
    print(select_all("SELECT * FROM users"))

    print(select_one("SELECT * FROM users WHERE user_id = %s", (1, )))


    return {
        "list": [
            dict(Author(1, "First book", None))
        ]
    }


@authors_controller.route("/", methods=["POST"])
def authors_list_post() -> dict:
    return {
        "book_id": 1
    }


@authors_controller.route("/<int:author_id>", methods=["GET"])
def authors_item_get(author_id: int) -> dict:
    return {
        "author_id": author_id
    }


@authors_controller.route("/<int:author_id>", methods=["PUT"])
def authors_item_put(author_id: int) -> dict:
    return {
        "author_id": author_id
    }


@authors_controller.route("/<int:author_id>", methods=["DELETE"])
def authors_item_delete(author_id: int) -> dict:
    return {
        "author_id": author_id
    }
