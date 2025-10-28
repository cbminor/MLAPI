import os
from io import BytesIO
import boto3
from app.core.config import settings

class DOSpaceClient:
    """ Digital Ocean Spaces Client for loading files """

    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            region_name=settings.DO_SPACE_REGION,
            endpoint_url=settings.DO_SPACE_ENDPOINT,
            aws_access_key_id=settings.DO_SPACE_ACCESS_KEY,
            aws_secret_access_key=settings.DO_SPACE_SECRET_KEY,
        )
        self.bucket = settings.DO_SPACE_NAME

    def get_file(self, file_key: str, cache_dir: str = "cache") -> BytesIO:
        """ Loads a file from the Digital Ocean Space """
        os.makedirs(cache_dir, exist_ok=True)
        local_path = os.path.join(cache_dir, os.path.basename(file_key))

        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                return BytesIO(f.read())
        
        response = self.s3.get_object(Bucket=self.bucket, Key=file_key)
        data = BytesIO(response['Body'].read())

        with open(local_path, 'wb') as f:
            f.write(data.getbuffer())

        return data
    
spaces = DOSpaceClient()