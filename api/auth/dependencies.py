from api.auth.jwt.dependencies import get_jwt_service
from api.auth.service import AuthService
from api.auth.users.dependencies import get_user_service


service = AuthService(get_user_service(), get_jwt_service())


def get_auth_service() -> AuthService:
    return service
