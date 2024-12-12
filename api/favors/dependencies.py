from fastapi import Depends

from api.favors.repository import FavorRepository
from api.favors.service import FavorService


def get_favor_service():
    return FavorService(FavorRepository())
