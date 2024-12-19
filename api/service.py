from strawberry.exceptions import GraphQLError

from api.logger import get_logger
from api.repository import Repository


class Service:
    def __init__(self, name: str, repository: Repository):
        self._logger = get_logger(name)
        self._repository = repository

    def _handle_error(self, message: str):
        self._logger.error(message)
        raise GraphQLError(message)
