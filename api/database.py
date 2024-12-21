from typing import AsyncGenerator
from prisma import Prisma
from contextlib import asynccontextmanager

from api.logger import get_logger
from api.main import app

prisma = Prisma()
logger = get_logger('Database')


@asynccontextmanager
async def db_session() -> AsyncGenerator[Prisma, None]:
    yield prisma


@app.on_event("startup")
async def on_startup():
    logger.info("Подключение к базе данных...")
    await prisma.connect()

@app.on_event("shutdown")
async def on_shutdown():
    logger.info("Отключение от базы данных...")
    await prisma.disconnect()
    