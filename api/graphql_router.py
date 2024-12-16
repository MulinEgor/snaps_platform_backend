import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry import Schema

from api.favors.endpoints.mutation import FavorMutation
from api.favors.endpoints.query import FavorQuery


@strawberry.type
class Query(FavorQuery):
    pass


@strawberry.type
class Mutation:
    @strawberry.field
    def favors(self) -> FavorMutation:
        return FavorMutation()


graphql_router = GraphQLRouter(
    Schema(Query, Mutation)
)
