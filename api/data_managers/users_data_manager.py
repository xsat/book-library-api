from ..models.user import User, build_user_from_dict
from ..db import select_one


def user_find_by_username(username: str) -> User | None:
    result = select_one(
        "SELECT u.`user_id`, u.`username`, u.`password_hash` " +
        "FROM `users` AS u " +
        "WHERE u.`username` = %s " +
        "LIMIT 1",
        (username, )
    )

    if result is not None:
        return build_user_from_dict(result)

    return None


# def book_create(book: Book) -> bool:
#     return True
#
#
# def book_update(book: Book) -> bool:
#     return True
#
#
# def book_delete(book: Book) -> bool:
#     return True