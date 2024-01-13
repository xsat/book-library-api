from typing import Self
from datetime import datetime
from ._model import Model


class Book(Model):
    def __init__(self,
                 book_id: int,
                 user_id: int,
                 title: str,
                 pages: int,
                 created_at: datetime) -> None:
        self.__book_id = book_id
        self.__user_id = user_id
        self.__title = title
        self.__pages = pages
        self.__created_at = created_at

    @property
    def book_id(self) -> int:
        return self.__book_id

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def pages(self) -> int:
        return self.__pages

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    def assign(self, book: Self) -> None:
        self.__book_id = book.book_id
        self.__user_id = book.user_id
        self.__title = book.title
        self.__pages = book.pages
        self.__created_at = book.created_at

    def json_serialize(self) -> dict:
        return {
            "book_id": self.book_id,
            "title": self.title,
            "pages": self.pages,
            "created_at": self.created_at
        }
