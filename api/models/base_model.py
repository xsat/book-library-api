class BaseModel:
    def json_serialize(self) -> dict:
        raise NotImplementedError
