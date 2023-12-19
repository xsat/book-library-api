from datetime import datetime


class Author:
    __author_id: int
    __name: str
    __created_at: datetime

    def __init__(self,
                 author_id: int,
                 name: str,
                 created_at: datetime | None = None) -> None:
        self.__author_id = author_id
        self.__name = name
        self.__created_at = created_at

    def __iter__(self) -> GeneratorExit:
        yield 'author_id', self.__author_id
        yield 'name', self.__name
        yield 'created_at', self.__created_at
