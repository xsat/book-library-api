from datetime import datetime
from ._model import Model


class Book(Model):
    def __init__(self,
                 book_id: int,
                 user_id: int,
                 title: str,
                 pages: int,
                 published_at: datetime,
                 created_at: datetime) -> None:
        self.__book_id = book_id
        self.__user_id = user_id
        self.__title = title
        self.__pages = pages
        self.__published_at = published_at
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
    def published_at(self) -> datetime:
        return self.__published_at

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    def json_serialize(self) -> dict:
        return {
            "book_id": self.book_id,
            "title": self.title,
            "pages": self.pages,
            "published_at": self.published_at,
            "created_at": self.created_at
        }
