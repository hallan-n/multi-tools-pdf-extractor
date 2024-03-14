from domain.models.pdf import PDF
from ..interfaces.pdf_repository import IPDFRepository

class PDFRepository(IPDFRepository):
    
    def find_by_id(self, pdf_id:int):
        # Implementar com o banco de dados
        return pdf_id

    def save(self, pdf: PDF):
        # Implementar com o banco de dados
        return pdf