import prisma

from api.database import db_session


class Repository:
    include = {}

    def __init__(self, table_name: str):
        self.table_name = table_name

    async def get(self, uuid: str) -> any:
        async with db_session() as session:
            table = self.get_table(session)
            return await table.find_unique(where={'uuid': uuid}, include=self.include)

    async def get_all(self, filters: dict) -> list[any]:
        async with db_session() as session:
            table = self.get_table(session)
            return await table.find_many(where=filters, include=self.include)

    async def create(self, data: dict) -> any:
        async with db_session() as session:
            table = self.get_table(session)
            return await table.create(data=data)

    async def update(self, uuid: str, data: dict) -> any:
        async with db_session() as session:
            table = self.get_table(session)
            return await table.update(where={'uuid': uuid}, data=data, include=self.include)

    async def delete(self, uuid: str) -> any:
        async with db_session() as session:
            table = self.get_table(session)
            return await table.delete(where={'uuid': uuid}, include=self.include)

    def get_table(self, session: prisma.Prisma):
        table = getattr(session, self.table_name)
        if not table:
            raise ValueError(f"Table {self.table_name} not found")
        return table
