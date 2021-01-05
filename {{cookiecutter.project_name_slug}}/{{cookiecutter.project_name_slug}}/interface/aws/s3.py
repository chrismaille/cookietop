from dataclasses import dataclass
from typing import Any

import boto3
from boto3 import Session  # type: ignore


@dataclass
class FileService:
    """File Service class backed by S3."""

    @property
    def client(self) -> Session.client:
        client = boto3.client("s3")
        return client

    def load(self, bucket: str, path: str, file: str) -> Any:
        """Read file from S3 bucket.

        :param bucket: bucket name
        :param path: path in bucket for file
        :param file: file name
        """
        key = f"{path}/{file}"
        file = self.client.get_object(Bucket=bucket, Key=key)
        return file["Body"].read()  # type: ignore
