import base64
from io import BytesIO

from fastapi import File, UploadFile
from fastapi.exceptions import HTTPException
from PyPDF2 import PdfReader, PdfWriter


class PDFUseCase:
    async def to_base64(self, files: list[UploadFile] = File(...)):
        base64_files = []
        for index, file in enumerate(files, start=1):
            if file.filename.lower().endswith(".pdf"):
                contents = await file.read()
                base64_encoded = base64.b64encode(contents).decode("utf-8")
                base64_files.append(
                    {
                        "filename": f"file-{str(index).zfill(2)}.pdf",
                        "base64": base64_encoded,
                    }
                )
        return base64_files

    async def renamePdfs(self, filename: str, files: list[UploadFile] = File(...)):
        renamed_files = []

        for index, file in enumerate(files, start=1):
            if file.filename.lower().endswith(".pdf"):
                new_filename = f"{filename}{str(index).zfill(2)}.pdf"
                content = await file.read()
                base64_content = base64.b64encode(content).decode("utf-8")
                renamed_files.append(
                    {"filename": new_filename, "base64_content": base64_content}
                )

        return renamed_files

    async def crack_pass(self, filename: str, files: list[UploadFile] = File(...)):
        decrypted_pdfs = []

        for index, file in enumerate(files, start=1):
            if file.filename.lower().endswith(".pdf"):
                try:
                    pdf_content = await file.read()
                    input_pdf = BytesIO(pdf_content)
                    reader = PdfReader(input_pdf)
                    if reader.is_encrypted:
                        for count in range(9999):
                            password = str(count).zfill(2)
                            if reader.decrypt(password) == 2:
                                break

                        writer = PdfWriter()
                        for page in reader.pages:
                            writer.add_page(page)
                        output_pdf = BytesIO()
                        writer.write(output_pdf)
                        output_pdf.seek(0)
                        base64_content = base64.b64encode(output_pdf.getvalue())
                    else:
                        output_pdf = input_pdf

                    decrypted_pdfs.append(
                        {
                            "filename": f"{filename}{str(index).zfill(2)}.pdf",
                            "base64_content": base64_content.decode("utf-8"),
                        }
                    )
                except Exception as e:
                    raise HTTPException(
                        status_code=500,
                        detail=f"Erro ao processar o PDF '{file.filename}': {str(e)}",
                    )

        return decrypted_pdfs

    async def get_metadatas(self, files: list[UploadFile] = File(...)):
        meta_list = []

        for file in files:
            if file.filename.lower().endswith(".pdf"):
                metadata = {}
                pdf_reader = PdfReader(file.file)
                metadata.setdefault("filename", file.filename)
                for meta in pdf_reader.metadata.keys():
                    metadata.setdefault(
                        str(meta).replace("/", "").lower(),
                        pdf_reader.metadata.get(meta),
                    )
                meta_list.append(metadata)

        return meta_list
