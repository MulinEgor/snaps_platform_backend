from contextlib import asynccontextmanager
import os
from aiobotocore.session import get_session
from fastapi import HTTPException, UploadFile

from api.service import Service


class S3Service(Service):
    def __init__(self):
        super().__init__(self.__class__.__name__, None)
        self._config = {
            "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
            "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
            "endpoint_url": os.getenv("ENDPOINT_URL"),
        }
        self._bucket_name = os.getenv("BUCKET_NAME")
        self._session = get_session()

    @asynccontextmanager
    async def _get_client(self):
        async with self._session.create_client("s3", **self._config) as client:
            yield client

    async def _get(self, name: str):
        self._logger.info(f"Checking if file with name {name} exists in S3")
        async with self._get_client() as client:
            try:
                await client.get_object(Bucket=self._bucket_name, Key=name)
                self._logger.info(f"File with name {name} exists in S3")
            except Exception as e:
                self._handle_error(
                    f"File with name {name} does not exist in S3", 404
                )

    async def upload(self, name: str, file: UploadFile) -> str:
        self._logger.info(f"Uploading file with name {name} to S3")
        async with self._get_client() as client:
            try:
                await client.put_object(Bucket=self._bucket_name, Key=name, Body=await file.read())
                self._logger.info(f"File with name {name} uploaded")
                return {
                    "url": f"{self._config['endpoint_url']}/{self._bucket_name}/{name}"
                }
            except Exception as e:
                self._handle_error(
                    f"Failed to upload file with name {name} to S3: {e}", 500
                )

    async def delete(self, name: str):
        self._logger.info(f"Deleting file with name {name} from S3")
        await self._get(name)  # check if data exists
        async with self._get_client() as client:
            try:
                await client.delete_object(Bucket=self._bucket_name, Key=name)
                self._logger.info(f"File with name {name} deleted")
            except Exception as e:
                self._handle_error(
                    f"Failed to delete file with name {name} from S3: {e}", 500
                )

    def _handle_error(self, message: str, status_code: int):
        self._logger.error(message)
        raise HTTPException(status_code=status_code, detail=message)
