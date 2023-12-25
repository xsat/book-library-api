from .base_model import BaseModel

from datetime import datetime

DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"

class UserToken(BaseModel):
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


def build_user_token_from_dict(data: dict) -> UserToken:
    if ("user_token_id" not in data
            or "user_id" not in data
            or "access_token" not in data
            or "created_at" not in data
            or "expired_at" not in data):
        raise ValueError(data)

    return UserToken(
        data["user_token_id"],
        data["user_id"],
        data["access_token"],
        datetime.strptime(data["created_at"], DATETIME_FORMAT),
        datetime.strptime(data["expired_at"], DATETIME_FORMAT)
    )
