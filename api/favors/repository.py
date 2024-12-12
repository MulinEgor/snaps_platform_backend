from prisma.models import Favor

from api.database import db_session
from api.favors.types.request import FavorCreateSchema, FavorUpdateSchema


class FavorRepository:
    async def get(self, uuid: str) -> Favor | None:
        async with db_session() as session:
            return await session.favor.find_unique(where={'uuid': uuid})

    async def get_all(self) -> list[Favor] | None:
        async with db_session() as session:
            return await session.favor.find_many()

    async def create(self, data: FavorCreateSchema) -> Favor:
        async with db_session() as session:
            return await session.favor.create(data=data.__dict__)

    async def update(self, uuid: str, data: FavorUpdateSchema) -> Favor:
        async with db_session() as session:
            return await session.favor.update(
                where={'uuid': uuid},
                data=data.to_dict()
            )

    async def delete(self, uuid: str) -> Favor:
        async with db_session() as session:
            return await session.favor.delete(where={'uuid': uuid})
