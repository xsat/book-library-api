from .base_model import BaseModel


class UserToken(BaseModel):
    def __init__(self,
                 user_token_id: int,
                 user_id: int,
                 access_token: str,
                 created_at: str,
                 expired_at: str):
        self.__user_token_id = user_token_id
        self.__user_id = user_id
        self.__access_token = access_token
        self.__created_at = created_at
        self.__expired_at = expired_at

    def json_serialize(self) -> dict:
        return {
            "access_token": self.__access_token,
            "created_at": self.__created_at,
            "expired_at": self.__expired_at
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
        data["created_at"],
        data["expired_at"],
    )
