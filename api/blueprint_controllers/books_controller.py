from flask import Blueprint


books_controller: Blueprint = Blueprint("books_controller", __name__, url_prefix="/books")


@books_controller.route("/", methods=["GET"])
def books_list_get() -> dict:
    return {
        "list": []
    }


@books_controller.route("/", methods=["POST"])
def books_list_post() -> dict:
    return {
        "book_id": 1
    }


@books_controller.route("/<int:book_id>", methods=["GET"])
def books_item_get(book_id: int) -> dict:
    return {
        "book_id": book_id
    }


@books_controller.route("/<int:book_id>", methods=["PUT"])
def books_item_put(book_id: int) -> dict:
    return {
        "book_id": book_id
    }


@books_controller.route("/<int:book_id>", methods=["DELETE"])
def books_item_delete(book_id: int) -> dict:
    return {
        "book_id": book_id
    }
