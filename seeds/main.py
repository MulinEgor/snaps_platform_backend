import asyncio

from api.s3.service import S3Service
from seeds.service import SeedService


async def main():
    service = SeedService(S3Service())
    await service.run()
    

if __name__ == '__main__':
    asyncio.run(main())
