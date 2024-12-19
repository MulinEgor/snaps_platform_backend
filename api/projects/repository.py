import prisma
from prisma.models import Project, Review

from api.database import db_session
from api.projects.schemas import ProjectCreateSchema, ProjectUpdateSchema, ReviewCreateSchema
from api.repository import Repository


class ProjectRepository(Repository):
    include = {
        'review': True
    }

    def __init__(self):
        super().__init__('project')

    async def get(self, uuid: str) -> Project | None:
        return await super().get(uuid)

    async def get_all(self, filters: ProjectUpdateSchema) -> list[Project]:
        return await super().get_all(filters.to_dict())

    async def create(self, data: ProjectCreateSchema) -> Project:
        async with db_session() as session:
            project_dict = data.__dict__
            review = await self._create_review(session, project_dict.pop('review'))
            if review:
                project_dict['review'] = {'connect': {'uuid': review.uuid}}
            project = await session.project.create(data=project_dict)
            project.review = review
            return project

    async def _create_review(self, session: prisma.Prisma, data: ReviewCreateSchema | None) -> Review | None:
        if data:
            return await session.review.create(data=data.__dict__)

    async def update(self, uuid: str, data: ProjectUpdateSchema) -> Project:
        async with db_session() as session:
            project_dict = data.__dict__
            review = project_dict.pop('review')
            project = await session.project.update(where={'uuid': uuid}, data=project_dict, include=self.include)
            if review:
                review = await session.review.update(where={'uuid': project.review_uuid}, data=review.__dict__)
                project.review = review
            return project

    async def delete(self, uuid: str) -> Project:
        return await super().delete(uuid)
