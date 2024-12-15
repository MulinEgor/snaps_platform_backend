import asyncio

from api.database import db_session
from api.logger import get_logger
from seeds.data import SeedDataSchema


async def run_seeds():
    logger = get_logger('Seeds')
    logger.info("Started running seeds")
    data_schema = SeedDataSchema()
    async with db_session() as session:
        for table_name, values in data_schema.model_dump().items():
            logger.info(f"Running seeds for table: {table_name}")
            table = getattr(session, table_name, None)

            if table:
                await table.create_many(data=values)
                logger.info(f"Inserted {len(values)} records into {
                    table_name} table.")
            else:
                logger.warning(
                    f"Table {table_name} model not found in Prisma client.")

    logger.info("Finished running seeds")


if __name__ == '__main__':
    asyncio.run(run_seeds())
