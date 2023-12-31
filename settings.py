import os
from uuid import uuid4
from dotenv import load_dotenv

from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    """App config"""

    DEPLOY: str = os.environ.get("DEPLOY", "local")
    RUN_ID: str = os.environ.get("RUN_ID", str(uuid4()))

    # AWS config
    AWS_REGION: str = os.environ.get("AWS_REGION", "us-east-1")
    AWS_ACCESS_KEY_ID: str = os.environ.get("AWS_ACCESS_KEY_ID", "dummy-key-id")
    AWS_SECRET_ACCESS_KEY: str = os.environ.get("AWS_SECRET_ACCESS_KEY", "dummy-key")

    BUCKET: str = os.environ.get("BUCKET", "dev-midas-news-scoring")

    LOGGER: str = "LOGGER"
