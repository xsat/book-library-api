from typing import Any

from flask import g
from MySQLdb import connect
from MySQLdb.connections import Connection
from MySQLdb.cursors import Cursor, DictCursor


def query_one(query: str, args: tuple[Any, ...] | dict[str, Any] | None = None) -> dict[str, Any] | None:
    db: Connection = _get_db()
    cursor: DictCursor = db.cursor(DictCursor)
    
    try:
        cursor.execute(query, args)

        result: dict = cursor.fetchone()
    finally:
        cursor.close()

    return result


def query_all(query: str, args: tuple[Any, ...] | dict[str, Any] | None = None) -> list[dict[str, Any]]:
    db: Connection = _get_db()
    cursor: DictCursor = db.cursor(DictCursor)

    try:
        cursor.execute(query, args)

        result: list[dict] = list(cursor.fetchall())
    finally:
        cursor.close()

    return result


def execute(query: str, args: tuple[Any, ...] | dict[str, Any] | None = None) -> int | None:
    db: Connection = _get_db()
    cursor: Cursor = db.cursor()

    try:
        cursor.execute(query, args)

        last_id: int | None = cursor.lastrowid
    finally:
        cursor.close()
        db.commit()

    return last_id


def _get_db() -> Connection:
    if "db" not in g:
        g.db = connect(host="localhost", user="root", password="123456", database="book_library")

    return g.get("db")
