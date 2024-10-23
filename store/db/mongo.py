from motor.motor_asyncio import AsyncIOMotorClient
from store.core.config import settings


class MongoClient:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(settings.DATABASE_URL)

    # GET method to return client
    def get(self) -> AsyncIOMotorClient:
        return self.client


db_client = MongoClient()
