from .base_model import BaseModel


class User(BaseModel):
    __user_id: int
    __username: str
    __password_hash: str

    def __init__(self,
                 user_id: int,
                 username: str,
                 password_hash: str):
        self.__user_id = user_id
        self.__username = username
        self.__password_hash = password_hash

    def user_id(self) -> int:
        return self.__user_id

    def username(self) -> str:
        return self.__username

    def password_hash(self) -> str:
        return self.__password_hash

    def json_serialize(self) -> dict:
        return {
            "user_id": self.__user_id,
            "username": self.__username
        }


def build_user_from_dict(data: dict) -> User:
    if ("user_id" not in data
            or "username" not in data
            or "password_hash" not in data):
        raise ValueError(data)

    return User(
        data["user_id"],
        data["username"],
        data["password_hash"]
    )
