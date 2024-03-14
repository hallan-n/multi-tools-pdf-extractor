from abc import ABC, abstractmethod

class PDFDataExtractorClient(ABC):
    @abstractmethod
    def classify(self):
        pass

    @abstractmethod
    def discovery(self):
        pass