from datetime import datetime


class Book:
    __book_id: int
    __user_id: int
    __title: str
    __description: str
    __created_at: datetime

    def __init__(self,
                 book_id: int,
                 user_id: int,
                 title: str,
                 description: str,
                 created_at: datetime) -> None:
        self.__book_id = book_id
        self.__user_id = user_id
        self.__title = title
        self.__description = description
        self.__created_at = created_at
