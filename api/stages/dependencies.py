from api.stages.repository import StageRepository
from api.stages.service import StageService


service = StageService(StageRepository())


def get_stage_service():
    return service
