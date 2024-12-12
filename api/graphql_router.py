from strawberry.fastapi import GraphQLRouter
from strawberry import Schema

from api.favors.endpoints.mutation import FavorMutation
from api.favors.endpoints.query import FavorQuery


class Query(FavorQuery):
    pass


class Mutation(FavorMutation):
    pass


graphql_router = GraphQLRouter(
    Schema(Query, Mutation)
)
