from ._model import Model


class BookAuthor(Model):
    def __init__(self,
                 book_author_id: int,
                 book_id: int,
                 author_id: int):
        self.__book_author_id = book_author_id
        self.__book_id = book_id
        self.__author_id = author_id

    @property
    def book_author_id(self) -> int:
        return self.__book_author_id

    @property
    def book_id(self) -> int:
        return self.__book_id

    @property
    def author_id(self) -> int:
        return self.__author_id

    def json_serialize(self) -> dict:
        return {}
