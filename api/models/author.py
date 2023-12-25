from .base_model import BaseModel


class Author(BaseModel):
    def __init__(self,
                 author_id: int,
                 name: str,
                 created_at: str) -> None:
        self.__author_id = author_id
        self.__name = name
        self.__created_at = created_at

    def json_serialize(self) -> dict:
        return {
            "author_id": self.__author_id,
            "name": self.__name,
            "created_at": self.__created_at
        }
