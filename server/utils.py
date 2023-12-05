import os
import uuid
from .logger import logging

logger = logging.getLogger(__package__)


def generate_uid() -> str:
    """Generate a unique identifier."""
    return uuid.uuid4().hex


def get_db_connection_url():
    match os.getenv("ENV", "dev").lower():
        case "prod":
            USER = os.environ["PROD_USER"]
            PSWD = os.environ["PROD_PASSWORD"]
            HOST = os.environ["PROD_HOST"]
            DB = os.environ["PROD_DBNAME"]
            logger.info(f"Connected to PROD database: {DB}!!")
        case "dev":
            USER = os.getenv("DEV_USER", "postgres")
            PSWD = os.getenv("DEV_PASSWORD", "")
            HOST = os.getenv("DEV_HOST")
            DB = os.getenv("DEV_DBNAME", "Testdb")
            logger.info(f"Connected to DEV database: {DB}!!")
        case _:
            raise Exception('Please set "ENV" environment to "prod" or "dev"')
    return f'postgresql://{USER}{":"+PSWD if PSWD else ""}@{HOST}/{DB}'
