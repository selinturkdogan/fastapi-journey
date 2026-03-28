from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import os
from dotenv import load_dotenv

from models.events import Event
from models.users import User

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")


async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["fastapi_db"]

    await init_beanie(database=db, document_models=[Event, User])