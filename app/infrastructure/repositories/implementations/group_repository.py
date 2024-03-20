from ..interfaces.persistence import Persistence
from ..config.connection import Connection


class GroupRepository(Persistence):
    def __init__(self):
        self.connection = Connection()

    async def create(self):
        pass

    async def read(self):
        pass

    async def update(self):
        pass

    async def delete(self):
        pass
