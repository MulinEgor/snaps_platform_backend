from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry import Schema

from api.config import APIConfig
from api.favors.endpoints.mutation import FavorMutation
from api.favors.endpoints.query import FavorQuery
from api.guarantees.endpoints.mutation import GuaranteeMutation
from api.projects.endpoints.mutation import ProjectMutation
from api.projects.endpoints.query import ProjectQuery
from api.guarantees.endpoints.query import GuaranteeQuery


# Loading environment variables
load_dotenv()

# Configuration API
config = APIConfig()
app = FastAPI(
    **config.model_dump()
)
app.add_middleware(
    CORSMiddleware,
    **config.cors.model_dump()
)


@strawberry.type
class Query(FavorQuery, GuaranteeQuery, ProjectQuery):
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


router = GraphQLRouter(
    Schema(Query, Mutation)
)

# including graphql router into FastAPI app
app.include_router(router, prefix="/graphql")
