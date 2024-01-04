from ._model import Model

from datetime import datetime


class UserToken(Model):
    __user_token_id: int
    __user_id: int
    __access_token: str
    __created_at: datetime
    __expired_at: datetime

    def __init__(self,
                 user_token_id: int,
                 user_id: int,
                 access_token: str,
                 created_at: datetime,
                 expired_at: datetime):
        self.__user_token_id = user_token_id
        self.__user_id = user_id
        self.__access_token = access_token
        self.__created_at = created_at
        self.__expired_at = expired_at

    def user_token_id(self) -> int:
        return self.__user_token_id

    def user_id(self) -> int:
        return self.__user_id

    def access_token(self) -> str:
        return self.__access_token

    def created_at(self) -> datetime:
        return self.__created_at

    def expired_at(self) -> datetime:
        return self.__expired_at

    def json_serialize(self) -> dict:
        return {
            "access_token": self.__access_token,
        }
