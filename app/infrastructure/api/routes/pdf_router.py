import base64
from io import BytesIO
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from PyPDF2 import PdfReader, PdfWriter

router = APIRouter()


@router.post("/pdf/base64")
async def to_base64(files: list[UploadFile] = File(...)):
    base64_files = []
    for index, file in enumerate(files, start=1):
        if file.filename.endswith(".pdf") or file.filename.endswith(".PDF"):
            contents = await file.read()
            base64_encoded = base64.b64encode(contents).decode("utf-8")
            base64_files.append(
                {
                    "filename": f"file-{str(index).zfill(2)}.pdf",
                    "base64": base64_encoded,
                }
            )
    return JSONResponse(content=base64_files)


@router.post("/pdf/rename")
async def to_base64(filename="file-", files: list[UploadFile] = File(...)):
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


@router.post("/pdf/pass")
async def crack_pass(files: list[UploadFile] = File(...), password: str = "999"):
    decrypted_pdfs = []

    for index, file in enumerate(files, start=1):
        if file.filename.lower().endswith(".pdf"):
            try:
                pdf_content = await file.read()
                input_pdf = BytesIO(pdf_content)
                reader = PdfReader(input_pdf)
                if reader.is_encrypted:
                    reader.decrypt(password)
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
                        "filename": f"file-{str(index).zfill(2)}.pdf",
                        "base64_content": base64_content.decode("utf-8"),
                    }
                )
            except Exception as e:
                raise HTTPException(
                    status_code=500,
                    detail=f"Erro ao processar o PDF '{file.filename}': {str(e)}",
                )

    return decrypted_pdfs


@router.post("/pdf/meta")
async def get_metadatas(files: list[UploadFile] = File(...)):
    meta_list = []
    for file in files:
        pdf_reader = PdfReader(file)
        meta = {
            "filename": file.filename,
            "title": pdf_reader.metadata.title,
            "author": pdf_reader.metadata.author,
            "creator": pdf_reader.metadata.creator,
            "producer": pdf_reader.metadata.producer,
            "creation_date": pdf_reader.metadata.creation_date,
            "modification_date": pdf_reader.metadata.modification_date,
        }
        meta_list.append(meta)
    return meta_list
