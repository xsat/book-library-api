from typing import Self

from ._model import Model


class User(Model):
    def __init__(self,
                 user_id: int,
                 username: str,
                 password_hash: str):
        self.__user_id = user_id
        self.__username = username
        self.__password_hash = password_hash

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password_hash(self) -> str:
        return self.__password_hash

    def assign(self, user: Self) -> None:
        self.__user_id = user.user_id
        self.__username = user.username
        self.__password_hash = user.password_hash

    def json_serialize(self) -> dict:
        return {
            "user_id": self.user_id,
            "username": self.username,
        }
