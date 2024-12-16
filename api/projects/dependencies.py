from api.projects.repository import ProjectRepository
from api.projects.service import ProjectService


service = ProjectService(ProjectRepository())


def get_project_service():
    return service
