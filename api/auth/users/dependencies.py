from api.auth.users.repository import UserRepository
from api.auth.users.service import UserService
from api.auth.roles.dependencies import get_role_service


service = UserService(UserRepository(), get_role_service())


def get_user_service():
    return service
