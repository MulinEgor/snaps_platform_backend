from api.auth.jwt.service import JWTService


service = JWTService()


def get_jwt_service() -> JWTService:
    return service
