from flask import Blueprint


authors_controller: Blueprint = Blueprint('authors_controller', __name__, url_prefix='/authors')


@authors_controller.route("/", methods=["GET"])
def authors_list_get() -> dict:
    return {
        "list": []
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
