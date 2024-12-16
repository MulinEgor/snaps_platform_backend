from strawberry.exceptions import GraphQLError

from api.logger import get_logger
from api.repository import Repository


class Service:
    def __init__(self, name: str, repository: Repository):
        self.logger = get_logger(name)
        self.repository = repository

    def handle_error(self, message: str):
        self.logger.error(message)
        raise GraphQLError(message)
