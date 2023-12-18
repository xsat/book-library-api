from flask import Flask
from flask import Blueprint


app: Flask = Flask(__name__)
app.config.from_mapping(DATABASE="")


@app.route("/books", methods=["GET"])
def books_list_get() -> dict:
    return {
        "list": []
    }


@app.route("/books", methods=["POST"])
def books_list_post() -> dict:
    return {
        "book_id": 1
    }


@app.route("/books/<int:book_id>", methods=["GET"])
def books_item_get(book_id: int) -> dict:
    return {
        "book_id": book_id
    }


@app.route("/books/<int:book_id>", methods=["PUT"])
def books_item_put(book_id: int) -> dict:
    return {
        "book_id": book_id
    }


@app.route("/books/<int:book_id>", methods=["DELETE"])
def books_item_delete(book_id: int) -> dict:
    return {
        "book_id": book_id
    }


@app.route("/authors", methods=["GET"])
def authors_list_get() -> dict:
    return {
        "list": []
    }


@app.route("/authors", methods=["POST"])
def authors_list_post() -> dict:
    return {
        "book_id": 1
    }


@app.route("/authors/<int:author_id>", methods=["GET"])
def authors_item_get(author_id: int) -> dict:
    return {
        "author_id": author_id
    }


@app.route("/authors/<int:author_id>", methods=["PUT"])
def authors_item_put(author_id: int) -> dict:
    return {
        "author_id": author_id
    }


@app.route("/authors/<int:author_id>", methods=["DELETE"])
def authors_item_delete(author_id: int) -> dict:
    return {
        "author_id": author_id
    }
