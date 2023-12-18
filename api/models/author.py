from datetime import datetime


class Author:
    __author_id: int
    __name: str
    __created_at: datetime

    def __init__(self,
                 book_id: int,
                 name: str,
                 created_at: datetime) -> None:
        self.__author_id = book_id
        self.__name = name
        self.__created_at = created_at
