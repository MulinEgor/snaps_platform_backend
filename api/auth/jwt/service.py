from datetime import datetime, timedelta
import os
from graphql import GraphQLError
from jose import JWTError, jwt

from api.auth.jwt.schemas import JWTGetSchema, JWTCreateSchema


class JWTService:
    def __init__(self):
        self._secret = os.getenv('JWT_ACCESS_SECRET')
        self._refresh_secret = os.getenv('JWT_REFRESH_SECRET')
        self._access_expire_days = int(os.getenv('JWT_ACCESS_EXPIRE_DAYS'))
        self._refresh_expire_days = int(os.getenv('JWT_REFRESH_EXPIRE_DAYS'))
        self._algorithm = "HS256"

    def create_tokens(self, schema: JWTCreateSchema) -> JWTGetSchema:
        access_token = self._create_token(
            schema,
            secret_key=self._secret,
            expires_delta=timedelta(days=self._access_expire_days)
        )

        refresh_token = self._create_token(
            schema,
            secret_key=self._refresh_secret,
            expires_delta=timedelta(days=self._refresh_expire_days)
        )

        return JWTGetSchema(
            access_token=access_token,
            refresh_token=refresh_token
        )

    def _create_token(self, schema: JWTCreateSchema, secret_key: str, expires_delta: timedelta) -> str:
        to_encode = schema.__dict__
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})

        return jwt.encode(to_encode, secret_key, algorithm=self._algorithm)

    def _verify_token(self, token: str, secret_key: str) -> dict:
        try:
            payload = jwt.decode(token, secret_key, algorithms=[
                self._algorithm
            ])
            if datetime.fromtimestamp(payload.get("exp")) < datetime.utcnow():
                raise GraphQLError(
                    message="Token expired"
                )
            return payload
        except JWTError as e:
            raise GraphQLError(
                message="Invalid token"
            )

    def refresh_tokens(self, refresh_token: str) -> JWTGetSchema:
        try:
            payload = self._verify_token(refresh_token, self._refresh_secret)
            payload.pop("exp", None)
            return self.create_tokens(JWTCreateSchema(**payload))
        except Exception:
            raise GraphQLError(
                message="Invalid refresh token"
            )

    def get_current_user(self, credentials: str) -> JWTCreateSchema:
        scheme, token = credentials.split()
        if scheme.lower() != "bearer":
            raise GraphQLError(
                message="Invalid authorization scheme"
            )
        payload = self._verify_token(token, self._secret)
        return JWTCreateSchema(**payload)

    # def set_exception_handler(self, app: FastAPI):
    #     @app.exception_handler(BadSignatureError)
    #     async def bad_signature_exception_handler(request: Request, exc: BadSignatureError):
    #         raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED,
    #             detail="Invalid token"
    #         )
