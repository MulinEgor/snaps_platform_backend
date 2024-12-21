from functools import wraps

from graphql import GraphQLError
from api.auth.jwt.dependencies import get_jwt_service
from strawberry.types import Info


def requires_admin(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        info: Info = args[1] if len(args) > 1 else kwargs.get('info')
        if not info:
            raise GraphQLError(
                message='Context information is not provided'
            )

        # getting request
        request = info.context.get("request")
        if not request:
            raise GraphQLError(
                message='Request not found in context'
            )

        # getting headers
        authorization: str = request.headers.get("Authorization")
        if not authorization:
            raise GraphQLError(
                message='This endpoint requires Authorization header'
            )

        user_data = get_jwt_service().get_current_user(authorization)

        if user_data.role_name != 'admin':
            raise GraphQLError(
                message='This endpoint requires admin role'
            )

        return await func(*args, **kwargs)
    return wrapper
