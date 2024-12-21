from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry import Schema

from api.config import APIConfig
from api.database import prisma
from api.favors.endpoints.mutation import FavorMutation
from api.favors.endpoints.query import FavorQuery
from api.guarantees.endpoints.mutation import GuaranteeMutation
from api.guarantees.endpoints.query import GuaranteeQuery
from api.projects.endpoints.mutation import ProjectMutation
from api.projects.endpoints.query import ProjectQuery
from api.questions.endpoints.mutation import QuestionMutation
from api.questions.endpoints.query import QuestionQuery
from api.stages.endpoints.mutation import StageMutation
from api.stages.endpoints.query import StageQuery
from api.requests.endpoints.mutation import RequestMutation
from api.requests.endpoints.query import RequestQuery
from api.auth.endpoints.mutation import AuthMutation
from api.auth.users.endpoints.mutation import UserMutation
from api.auth.users.endpoints.query import UserQuery
from api.auth.roles.endpoints.mutation import RoleMutation
from api.auth.roles.endpoints.query import RoleQuery
from api.s3.endpoints.routes import router as s3_router


# Loading environment variables
load_dotenv()


@strawberry.type
class Query(
    FavorQuery,
    GuaranteeQuery,
    ProjectQuery,
    StageQuery,
    QuestionQuery,
    RequestQuery,
    UserQuery,
    RoleQuery
):
    pass


@strawberry.type
class Mutation:
    @strawberry.field
    def favors(self) -> FavorMutation:
        return FavorMutation()

    @strawberry.field
    def guarantees(self) -> GuaranteeMutation:
        return GuaranteeMutation()

    @strawberry.field
    def projects(self) -> ProjectMutation:
        return ProjectMutation()

    @strawberry.field
    def stages(self) -> StageMutation:
        return StageMutation()

    @strawberry.field
    def questions(self) -> QuestionMutation:
        return QuestionMutation()

    @strawberry.field
    def requests(self) -> RequestMutation:
        return RequestMutation()

    @strawberry.field
    def auth(self) -> AuthMutation:
        return AuthMutation()

    @strawberry.field
    def users(self) -> UserMutation:
        return UserMutation()

    @strawberry.field
    def roles(self) -> RoleMutation:
        return RoleMutation()


async def get_context(request: Request):
    return {"request": request}


graphql_router = GraphQLRouter(
    Schema(Query, Mutation),
    prefix="/graphql",
    context_getter=get_context,
    include_in_schema=False
)


# FastAPI configuration
config = APIConfig()
app = FastAPI(
    **config.model_dump()
)
app.add_middleware(
    CORSMiddleware,
    **config.cors.model_dump()
)


@app.on_event("startup")
async def on_startup():
    await prisma.connect()


@app.on_event("shutdown")
async def on_shutdown():
    await prisma.disconnect()
    

# including routers into FastAPI app
routers = [
    graphql_router,
    s3_router
]
for router in routers:
    app.include_router(router)
