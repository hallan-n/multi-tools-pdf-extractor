from ..interfaces.persistence import Persistence
from ..config.connection import Connection


class TemplateRepository(Persistence):
    def __init__(self):
        self.connection = Connection()

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
