from abc import ABC, abstractmethod
from domain.models.pdf import PDF

class IPDFRepository(ABC):
    @abstractmethod
    def find_by_id(self, pdf_id:int):
        pass

    @abstractmethod
    def save(self, pdf: PDF):
        pass