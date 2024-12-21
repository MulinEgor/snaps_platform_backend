from typing import AsyncGenerator
from prisma import Prisma
from contextlib import asynccontextmanager


prisma = Prisma()


@asynccontextmanager
async def db_session() -> AsyncGenerator[Prisma, None]:
    yield prisma
