from api.requests.repository import RequestRepository
from api.requests.service import RequestService


service = RequestService(RequestRepository())


def get_request_service():
    return service
