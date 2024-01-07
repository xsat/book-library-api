from ._model import Model

from datetime import datetime
from typing import Self


class Author(Model):
    def __init__(self,
                 author_id: int,
                 user_id: int,
                 name: str,
                 created_at: datetime) -> None:
        self.__author_id = author_id
        self.__user_id = user_id
        self.__name = name
        self.__created_at = created_at

    @property
    def author_id(self) -> int:
        return self.__author_id

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    def assign(self, author: Self) -> None:
        self.__author_id = author.author_id
        self.__user_id = author.user_id
        self.__name = author.username
        self.__created_at = author.created_at

    def json_serialize(self) -> dict:
        return {
            "author_id": self.author_id,
            "name": self.name,
        }
