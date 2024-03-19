from abc import ABC, abstractmethod


class DataParser(ABC):
    @abstractmethod
    def to_schema(self):
        pass

    @abstractmethod
    def to_model(self):
        pass
