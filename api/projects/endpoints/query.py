import strawberry
import strawberry.field_extensions

from api.projects.dependencies import get_project_service
from api.projects.schemas import ProjectUpdateSchema, ProjectGetSchema


@strawberry.type
class ProjectQuery:
    @strawberry.field
    async def projects(
        self,
        filters: ProjectUpdateSchema
    ) -> list[ProjectGetSchema]:
        return await get_project_service().get_all(filters)
