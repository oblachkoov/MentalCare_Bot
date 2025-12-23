import os
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

load_dotenv()

TOKEN = os.getenv("TOKEN")

engine = create_async_engine(
    "postgresql+asyncpg://postgres:111@localhost:5432/MentalCareBot",
    echo=False,
    pool_pre_ping=True,
    pool_size=2000,
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
)