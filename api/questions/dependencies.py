from api.questions.repository import QuestionRepository
from api.questions.service import QuestionService


service = QuestionService(QuestionRepository())


def get_question_service():
    return service
