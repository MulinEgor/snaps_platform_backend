from fastapi import APIRouter, File, UploadFile, status

from api.s3.dependencies import get_s3_service


router = APIRouter(
    prefix="/s3",
    tags=["s3"]
)


@router.post("/", status_code=status.HTTP_200_OK)
async def upload_file(name: str, file: UploadFile = File(...)):
    return await get_s3_service().upload(name, file)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_file(name: str):
    return await get_s3_service().delete(name)
