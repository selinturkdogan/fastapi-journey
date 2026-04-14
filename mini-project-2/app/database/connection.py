from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import os
from dotenv import load_dotenv

from models.events import Event
from models.users import User

load_dotenv()


class Settings:
    async def initialize_database(self):
        database_url = os.getenv("DATABASE_URL", "mongodb://localhost:27017/planner")
        client = AsyncIOMotorClient(database_url)
        db_name = database_url.rsplit("/", 1)[-1] or "planner"
        db = client[db_name]
        await init_beanie(database=db, document_models=[Event, User])