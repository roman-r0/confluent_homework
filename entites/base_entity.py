import abc


class BaseEntity(abc.ABC):
    def to_json(self):
        return self.__dict__


class BaseGenerateRandom(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def generate_random():
        pass
