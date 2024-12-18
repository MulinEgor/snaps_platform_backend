from typing import AsyncGenerator
from prisma import Prisma
from contextlib import asynccontextmanager

from api.logger import get_logger


prisma = Prisma()
logger = get_logger('Database')


@asynccontextmanager
async def db_session() -> AsyncGenerator[Prisma, None]:
    if not prisma.is_connected():
        logger.info('Connecting to database...')
        await prisma.connect()
    try:
        yield prisma
    except Exception as e:
        logger.error(e)
    finally:
        await prisma.disconnect()
