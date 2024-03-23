from fastapi import UploadFile, File

import base64


class PDFUseCase:
    async def to_base64(self, file: UploadFile = File(...)):
        if not file.filename.endswith(".pdf"):
            return False
        try:
            contents = await file.read()
            encoded_pdf = base64.b64encode(contents).decode("utf-8")
            return encoded_pdf
        except Exception as e:
            raise e

    def renamePdfs(self):
        ...

    def crack_pass(self):
        ...

    def get_metadatas(self):
        ...
