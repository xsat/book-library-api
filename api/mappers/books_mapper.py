from datetime import datetime

from ..db import query_one, query_all, execute
from ..datetime import today_datetime, to_mysql_datetime
from ..models.user import User
from ..models.book import Book
from ..binders.list_binder import ListBinder
from ..binders.book_binder import BookBinder


def books_find_by_binder_and_user(list_binder: ListBinder, user: User) -> list[Book]:
    select_query: str = "SELECT b.`book_id`, b.`user_id`, b.`title`, b.`pages`, b.`created_at`"
    from_query: str = "FROM `books` AS b"
    where_query: str = "WHERE b.`user_id` = %s"
    args: tuple = (user.user_id, )

    if len(list_binder.search) > 0:
        where_query = f"{where_query} AND b.`title` LIKE %s"
        args = args + (f"%{list_binder.search}%", )

    order_query: str = f"ORDER BY b.`{list_binder.order}` {list_binder.sort}"
    limit_offset_query: str = "LIMIT %s OFFSET %s"
    args = args + (list_binder.limit, list_binder.offset)

    results: list[dict] = query_all(
        f"{select_query} {from_query} {where_query} {order_query} {limit_offset_query}",
        args
    )

    print(results)

    books: list[Book] = []

    for item in results:
        books.append(_build_book_from_dict(item))

    return books


def books_total_by_binder_and_user(list_binder: ListBinder, user: User) -> int:
    select_query: str = "SELECT COUNT(b.`book_id`) AS `count`"
    from_query: str = "FROM `books` AS b"
    where_query: str = "WHERE b.`user_id` = %s"
    args: tuple = (user.user_id,)

    if len(list_binder.search) > 0:
        where_query = f"{where_query} AND b.`title` LIKE %s"
        args = args + (f"%{list_binder.search}%",)

    result: dict | None = query_one(
        f"{select_query} {from_query} {where_query}",
        args
    )

    if result is not None and "count" in result:
        return result['count']

    return 0


def book_find_by_id_and_user(book_id: int, user: User) -> Book | None:
    result: dict | None = query_one(
        "SELECT b.`book_id`, b.`user_id`, b.`title`, b.`pages`, b.`created_at` " +
        "FROM `books` AS b " +
        "WHERE b.`book_id` = %s AND b.`user_id` = %s " +
        "LIMIT 1",
        (book_id, user.user_id)
    )

    if result is not None:
        return _build_book_from_dict(result)

    return None


def book_create_by_binder_and_user(book_binder: BookBinder, user: User) -> Book:
    created_at: datetime = today_datetime()
    book_id: int | None = execute(
        "INSERT INTO `books` (`user_id`, `title`, `pages`, `created_at`) " +
        "VALUE (%s, %s, %s, %s)",
        (user.user_id, book_binder.title, book_binder.pages, to_mysql_datetime(created_at))
    )

    return Book(book_id, user.user_id, book_binder.title, book_binder.pages, created_at)


def book_update_by_binder(book: Book, book_binder: BookBinder) -> None:
    updated_book: Book = Book(book.book_id, book.user_id, book_binder.title, book_binder.pages, book.created_at)
    book.assign(updated_book)

    execute(
        "UPDATE `books` AS b " +
        "SET b.`title` = %s, b.`pages` = %s " +
        "WHERE b.`book_id` = %s AND b.`user_id` = %s",
        (book.title, book.pages, book.book_id, book.user_id)
    )


def book_delete(book: Book) -> None:
    execute(
        "DELETE FROM `books` AS a " +
        "WHERE a.`book_id` = %s AND a.`user_id` = %s",
        (book.book_id, book.user_id)
    )


def _build_book_from_dict(data: dict) -> Book:
    if ("book_id" not in data
            or "user_id" not in data
            or "title" not in data
            or "pages" not in data
            or "created_at" not in data):
        raise ValueError(data)

    return Book(
        data["book_id"],
        data["user_id"],
        data["title"],
        data["pages"],
        data["created_at"]
    )
