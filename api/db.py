from MySQLdb.cursors import Cursor, DictCursor
from MySQLdb import connect, Connection
from flask import g


def select_one(query: str, args: tuple | dict | None = None) -> dict | None:
    db: Connection = _get_db()
    cursor: DictCursor = db.cursor(DictCursor)

    try:
        cursor.execute(query, args)

        result: dict = cursor.fetchone()
    finally:
        cursor.close()

    return result


def select_all(query: str, args: tuple | dict | None = None) -> list[dict]:
    db: Connection = _get_db()
    cursor: DictCursor = db.cursor(DictCursor)

    try:
        cursor.execute(query, args)

        result: list[dict] = []

        for row in cursor.fetchall():
            result.append(row)
    finally:
        cursor.close()

    return result


def execute(query: str, args: tuple | dict | None = None) -> int | None:
    db: Connection = _get_db()
    cursor: Cursor = db.cursor()

    try:
        cursor.execute(query, args)

        last_id: int | None = cursor.lastrowid
    finally:
        cursor.close()

    return last_id


def _get_db() -> Connection:
    if "db" not in g:
        g.db = connect(host="localhost", user="root", password="123456", database="book_library")

    return g.db
