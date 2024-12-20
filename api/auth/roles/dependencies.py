from api.auth.roles.repository import RoleRepository
from api.auth.roles.service import RoleService


service = RoleService(RoleRepository())


def get_role_service():
    return service
