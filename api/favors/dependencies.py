from api.favors.repository import FavorRepository
from api.favors.service import FavorService


service = FavorService(FavorRepository())


def get_favor_service():
    return service
