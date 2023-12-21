from MySQLdb import connect, Connection
from flask import g


def get_db() -> Connection:
    if "db" not in g:
        g.db = connect(host="localhost", user="root", password="123456", database="book_library")

    return g.db
