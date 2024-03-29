from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import UploadFile, File
import base64

router = APIRouter()


@router.post("/pdf/base64")
async def to_base64(files: list[UploadFile] = File(...)):
    base64_files = []
    for file in files:
        if file.filename.endswith(".pdf") or file.filename.endswith(".PDF"):
            contents = await file.read()
            base64_encoded = base64.b64encode(contents).decode("utf-8")
            base64_files.append({"filename": file.filename, "base64": base64_encoded})
    return JSONResponse(content=base64_files)


@router.post("/pdf/rename")
async def to_base64(filename="file-", files: list[UploadFile] = File(...)):
    renamed_files = []
    for index, file in enumerate(files, start=1):
        enum = str(index).zfill(2)
        new_filename = f"{filename}{enum}.pdf"
        content = await file.read()
        base64_content = base64.b64encode(content).decode("utf-8")
        renamed_files.append(
            {"filename": new_filename, "base64_content": base64_content}
        )
    return renamed_files


@router.post("/pdf")
async def crack_pass():
    pass


@router.post("/pdf")
async def get_metadatas():
    pass
