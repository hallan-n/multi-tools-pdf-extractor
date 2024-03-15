from abc import ABC, abstractmethod


class Persistence(ABC):
    @abstractmethod
    async def create(self):
        pass

    @abstractmethod
    async def read(self):
        pass

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    async def delete(self):
        pass
