import json
import os
from api.auth.users.service import UserService
from api.database import db_session
from api.logger import get_logger
from api.s3.service import S3Service


class SeedService:
    def __init__(self, s3_service: S3Service):
        self._logger = get_logger('SeedService')
        self._data = {}
        self._s3_service = s3_service
        self._s3_seeds_data_path = os.getenv('S3_SEEDS_DATA_PATH')
        
    async def read_data(self):
        self._logger.info(f"Reading data from {self._s3_seeds_data_path}")
        await self._s3_service.download(self._s3_seeds_data_path, self._s3_seeds_data_path)
        with open(self._s3_seeds_data_path, 'r') as file:
            self._data = json.load(file)
        self._logger.info(f"Data read from {self._s3_seeds_data_path}")
        os.remove(self._s3_seeds_data_path)
        
    async def run(self):
        self._logger.info("Running seeds")
        await self.read_data()
        async with db_session() as session:
            for table_name, values in self._data.items():
                self._logger.info(f"Running seeds for table: {table_name}")
                table = getattr(session, table_name, None)

                if table:
                    if table_name == 'user':  # add to them admin role as well
                        admin_role = await session.role.find_first(where={'name': 'admin'})
                        if not admin_role:
                            self._logger.error(
                                "Admin role not found, can't create users")
                            raise Exception(
                                "Admin role not found, cant create users")
                        users: list[dict] = []
                        for user in values:
                            users.append(
                                {
                                    'email': user['email'],
                                    'hashed_password': UserService.hash_password(
                                        user['password']
                                    ),
                                    'role_uuid': admin_role.uuid
                                }
                            )
                        values = users

                    await table.create_many(data=values)
                    self._logger.info(f"Inserted {len(values)} records into {
                        table_name} table.")
                else:
                    self._logger.error(
                        f"Table {table_name} model not found in Prisma client.")

        self._logger.info("Finished running seeds")
