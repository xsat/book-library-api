from ..models.author import Author
from ..db import query_one, query_all, execute
from ..datetime import from_mysql_datetime


def author_create(author: Author) -> bool:
    return True


def author_update(author: Author) -> bool:
    return True


def author_delete(author: Author) -> bool:
    return True


def _build_author_from_dict(data: dict) -> Author:
    if ("author_id" not in data
            or "name" not in data
            or "created_at" not in data):
        raise ValueError(data)

    return Author(
        data["author_id"],
        data["name"],
        from_mysql_datetime(data["created_at"])
    )
