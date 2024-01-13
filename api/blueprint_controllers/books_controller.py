from flask import Blueprint, request

from ..auth import authorize_user, AuthorizedUser
from ..exeptions import BadRequestError, NotFoundError
from ..models.book import Book
from ..binders.list_binder import ListBinder
from ..binders.book_binder import BookBinder
from ..validators.list_validation import ListValidation
from ..validators.book_validation import BookValidation
from ..mappers.books_mapper import (
    books_find_by_binder_and_user,
    books_total_by_binder_and_user,
    book_create_by_binder_and_user,
    book_find_by_id_and_user,
    book_update_by_binder,
    book_delete
)


books_controller: Blueprint = Blueprint("books_controller", __name__, url_prefix="/books")


@books_controller.route("/", methods=["GET"])
@authorize_user
def books_list(authorized_user: AuthorizedUser) -> dict:
    list_binder: ListBinder = ListBinder(request)
    list_validation: ListValidation = ListValidation(list_binder)
    if not list_validation.is_valid():
        raise BadRequestError(list_validation.error_message())

    books: list[Book] = books_find_by_binder_and_user(list_binder, authorized_user.user)
    total: int = books_total_by_binder_and_user(list_binder, authorized_user.user)

    return {
        "order": list_binder.order,
        "sort": list_binder.sort,
        "offset": list_binder.offset,
        "limit": list_binder.limit,
        "total": total,
        "items": books,
    }


@books_controller.route("/<int:book_id>", methods=["GET"])
@authorize_user
def books_book(book_id: int, authorized_user: AuthorizedUser) -> dict:
    book: Book | None = book_find_by_id_and_user(book_id, authorized_user.user)
    if book is None:
        raise NotFoundError()

    return {
        "book": book,
    }


@books_controller.route("/", methods=["POST"])
@authorize_user
def books_book_create(authorized_user: AuthorizedUser) -> dict:
    book_binder: BookBinder = BookBinder(request)
    book_validation: BookValidation = BookValidation(book_binder)
    if not book_validation.is_valid():
        raise BadRequestError(book_validation.error_message())

    book: Book = book_create_by_binder_and_user(book_binder, authorized_user.user)

    return {
        "book": book,
    }


@books_controller.route("/<int:book_id>", methods=["PUT"])
@authorize_user
def books_book_update(book_id: int, authorized_user: AuthorizedUser) -> dict:
    book: Book | None = book_find_by_id_and_user(book_id, authorized_user.user)
    if book is None:
        raise NotFoundError()

    book_binder: BookBinder = BookBinder(request)
    book_validation: BookValidation = BookValidation(book_binder)
    if not book_validation.is_valid():
        raise BadRequestError(book_validation.error_message())

    book_update_by_binder(book, book_binder)

    return {
        "book": book,
    }


@books_controller.route("/<int:book_id>", methods=["DELETE"])
@authorize_user
def books_book_delete(book_id: int, authorized_user: AuthorizedUser) -> dict:
    book: Book | None = book_find_by_id_and_user(book_id, authorized_user.user)
    if book is None:
        raise NotFoundError()

    book_delete(book)

    return {
        "book": None,
    }
