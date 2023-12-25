from .base_model import BaseModel


class User(BaseModel):
    def __init__(self, data):
        self.__data = data
        pass

    def json_serialize(self) -> dict:
        return {"data": self.__data}
