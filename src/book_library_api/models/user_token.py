from datetime import datetime

from ._model import Model


class UserToken(Model):
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

    @property
    def user_token_id(self) -> int:
        return self.__user_token_id

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def access_token(self) -> str:
        return self.__access_token

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    @property
    def expired_at(self) -> datetime:
        return self.__expired_at

    def json_serialize(self) -> dict:
        return {
            "access_token": self.access_token,
        }
