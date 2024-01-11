from datetime import datetime

from ..db import query_one, query_all, execute
from ..datetime import today_datetime, to_mysql_datetime
from ..models.user import User
from ..models.author import Author
from ..binders.list_binder import ListBinder
from ..binders.author_binder import AuthorBinder


def authors_find_by_binder_and_user(list_binder: ListBinder, user: User) -> list[Author]:
    results = query_all(
        "SELECT a.`author_id`, a.`user_id`, a.`name`, a.`created_at` " +
        "FROM `authors` AS a "
        "WHERE a.`user_id` = %s " +
        "ORDER BY %s %s " +
        "LIMIT %s OFFSET %s",
        (user.user_id, list_binder.order, list_binder.sort, list_binder.limit, list_binder.offset)
    )

    authors: list[Author] = []

    for item in results:
        authors.append(_build_author_from_dict(item))

    return authors


def authors_total_by_binder_and_user(list_binder: ListBinder, user: User) -> int:
    result = query_one(
        "SELECT COUNT(a.`author_id`) AS `count` " +
        "FROM `authors` AS a "
        "WHERE a.`user_id` = %s",
        (user.user_id, )
    )

    if result is not None and "count" in result:
        return result['count']

    return 0


def author_find_by_id_and_user(author_id: int, user: User) -> Author | None:
    result = query_one(
        "SELECT a.`author_id`, a.`user_id`, a.`name`, a.`created_at` " +
        "FROM `authors` AS a "
        "WHERE a.`author_id` = %s AND a.`user_id` = %s " +
        "LIMIT 1",
        (author_id, user.user_id)
    )

    if result is not None:
        return _build_author_from_dict(result)

    return None


def author_create_by_binder_and_user(author_binder: AuthorBinder, user: User) -> Author:
    created_at: datetime = today_datetime()
    author_id: int | None = execute(
        "INSERT INTO `authors` (`user_id`, `name`, `created_at`) " +
        "VALUE (%s, %s, %s)",
        (user.user_id, author_binder.name, to_mysql_datetime(created_at))
    )

    return Author(author_id, user.user_id, author_binder.name, created_at)


def author_update_by_binder(author: Author, author_binder: AuthorBinder) -> None:
    updated_author: Author = Author(author.author_id, author.user_id, author_binder.name, author.created_at)
    author.assign(updated_author)

    execute(
        "UPDATE `authors` AS a " +
        "SET a.`name` = %s " +
        "WHERE a.`author_id` = %s",
        (author.name, author.author_id, )
    )


def author_delete(author: Author) -> None:
    execute(
        "DELETE FROM `authors` AS a " +
        "WHERE a.`author_id` = %s AND a.`user_id` = %s",
        (author.author_id, author.user_id)
    )


def _build_author_from_dict(data: dict) -> Author:
    if ("author_id" not in data
            or "user_id" not in data
            or "name" not in data
            or "created_at" not in data):
        raise ValueError(data)

    return Author(
        data["author_id"],
        data["user_id"],
        data["name"],
        data["created_at"]
    )
