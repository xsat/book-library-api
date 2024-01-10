from flask import Blueprint, request

from ..auth import authorize_user, AuthorizedUser
from ..exeptions import BadRequestError, NotFoundError

from ..models.author import Author
from ..binders.list_binder import ListBinder
from ..binders.author_binder import AuthorBinder
from ..validators.author_validation import AuthorValidation
from ..mappers.authors_mapper import (
    authors_find_by_binder_and_user,
    authors_total_by_binder_and_user,
    author_create_by_binder_and_user,
    author_find_by_id_and_user,
    author_update_by_binder,
    author_delete
)


authors_controller: Blueprint = Blueprint("authors_controller", __name__, url_prefix="/authors")


@authors_controller.route("/", methods=["GET"])
@authorize_user
def authors_list(authorized_user: AuthorizedUser) -> dict:
    list_binder: ListBinder = ListBinder(request)
    authors: list[Author] = authors_find_by_binder_and_user(list_binder, authorized_user.user)
    total: int = authors_total_by_binder_and_user(list_binder, authorized_user.user)

    return {
        "items": authors,
        "limit": list_binder.limit,
        "offset": list_binder.offset,
        "total": total,
    }


@authors_controller.route("/<int:author_id>", methods=["GET"])
@authorize_user
def authors_author(author_id: int, authorized_user: AuthorizedUser) -> dict:
    author: Author | None = author_find_by_id_and_user(author_id, authorized_user.user)
    if author is None:
        raise NotFoundError("Author not found")

    return {
        "author": author
    }


@authors_controller.route("/", methods=["POST"])
@authorize_user
def authors_author_create(authorized_user: AuthorizedUser) -> dict:
    author_binder: AuthorBinder = AuthorBinder(request)
    author_validation: AuthorValidation = AuthorValidation(author_binder)
    if not author_validation.is_valid():
        raise BadRequestError(author_validation.error_message())

    author: Author = author_create_by_binder_and_user(author_binder, authorized_user.user)

    return {
        "author": author,
    }


@authors_controller.route("/<int:author_id>", methods=["PUT"])
@authorize_user
def authors_author_update(author_id: int, authorized_user: AuthorizedUser) -> dict:
    author: Author | None = author_find_by_id_and_user(author_id, authorized_user.user)
    if author is None:
        raise NotFoundError("Author not found")

    author_binder: AuthorBinder = AuthorBinder(request)
    author_validation: AuthorValidation = AuthorValidation(author_binder)
    if not author_validation.is_valid():
        raise BadRequestError(author_validation.error_message())

    author_update_by_binder(author, author_binder)

    return {
        "author": author,
    }


@authors_controller.route("/<int:author_id>", methods=["DELETE"])
@authorize_user
def authors_author_delete(author_id: int, authorized_user: AuthorizedUser) -> dict:
    author: Author | None = author_find_by_id_and_user(author_id, authorized_user.user)
    if author is None:
        raise NotFoundError("Author not found")

    author_delete(author)

    return {
        "author": None,
    }
