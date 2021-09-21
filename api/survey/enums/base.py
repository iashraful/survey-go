import enum


class BaseEnum(enum.Enum):
    @classmethod
    def list_of_values(cls, datatype=str):
        return [e.value for e in cls]
