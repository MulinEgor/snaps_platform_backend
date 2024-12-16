from prisma.models import Project

from api.database import db_session
from api.projects.types.request import ProjectSchema, ProjectOptionalSchema
from api.repository import Repository


class ProjectRepository(Repository):
    def __init__(self):
        super().__init__('project')

    async def get(self, uuid: str) -> Project | None:
        return await super().get(uuid)

    async def get_all(self, filters: ProjectOptionalSchema) -> list[Project] | None:
        return await super().get_all(filters.to_dict())

    async def create(self, data: ProjectSchema) -> Project:
        async with db_session() as session:
            # project_dict = data.__dict__
            # review_dict = project_dict.pop('review', None)
            # review: Review | None = None
            # if review_dict:
            #     review = await session.review.create(data=review_dict)

            # project = await session.project.create(data={
            #     **project_dict,
            #     'review': {'connect': {'uuid': review.uuid}} if review else None
            # })
            project = await session.project.create(data=data.__dict__)
            return project

    async def update(self, uuid: str, data: ProjectOptionalSchema) -> Project:
        return await super().update(uuid, data.to_dict())

    async def delete(self, uuid: str) -> Project:
        return await super().delete(uuid)
