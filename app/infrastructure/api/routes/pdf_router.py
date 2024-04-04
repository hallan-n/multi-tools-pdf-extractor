from fastapi import APIRouter, UploadFile, File
from app.domain.use_cases.pdf_use_case import PDFUseCase

router = APIRouter(tags=["PDF"])
pdf_cases = PDFUseCase()


@router.post("/pdf/base64")
async def to_base64(files: list[UploadFile] = File(...)):
    base64_files = await pdf_cases.to_base64(files)
    return base64_files


@router.post("/pdf/rename")
async def renamePdfs(filename="file-", files: list[UploadFile] = File(...)):
    renamed_files = await pdf_cases.renamePdfs(filename, files)
    return renamed_files


@router.post("/pdf/pass")
async def crack_pass(filename: str = "file-", files: list[UploadFile] = File(...)):
    decrypted_pdfs = await pdf_cases.crack_pass(filename, files)
    return decrypted_pdfs


@router.post("/pdf/meta")
async def get_metadatas(files: list[UploadFile] = File(...)):
    meta_list = await pdf_cases.get_metadatas(files)
    return meta_list
