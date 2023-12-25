from .base_model import BaseModel


class Book(BaseModel):
    def __init__(self,
                 book_id: int,
                 user_id: int,
                 title: str,
                 description: str,
                 created_at: str) -> None:
        self.__book_id = book_id
        self.__user_id = user_id
        self.__title = title
        self.__description = description
        self.__created_at = created_at

    def json_serialize(self) -> dict:
        return {
            "book_id": self.__book_id,
            "title": self.__title,
            "description": self.__description,
            "created_at": self.__created_at
        }
