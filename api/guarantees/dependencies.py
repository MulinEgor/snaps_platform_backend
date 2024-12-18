from api.guarantees.repository import GuaranteeRepository
from api.guarantees.service import GuaranteeService


service = GuaranteeService(GuaranteeRepository())


def get_guarantee_service():
    return service
