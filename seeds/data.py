import prisma
from pydantic import BaseModel

from api.favors.types.request import FavorCreateSchema


favors_data = [
    FavorCreateSchema(
        name='Старт',
        includes=[
            'Корпоративный сайт до 5 страниц',
            'Адаптивный дизайн',
            'Базовое SEO',
            '1 месяц поддержки'
        ],
        duration_weeks=3,
        price=150000,
        application_type=prisma.models.enums.ApplicationType.WEB
    ),
    FavorCreateSchema(
        name='Бизнес',
        includes=[
            'Интернет магазин',
            'Платежные системы',
            'Личный кабинет',
            '3 месяца поддержки'
        ],
        duration_weeks=6,
        price=350000,
        application_type=prisma.models.enums.ApplicationType.WEB
    ),
    FavorCreateSchema(
        name='Премиум',
        includes=[
            'Высоконагруженные проекты',
            'Индивидуальная архитектура',
            'Сложные интеграции',
            '6 месяц поддержки'
        ],
        duration_weeks=8,
        price=600000,
        application_type=prisma.models.enums.ApplicationType.WEB
    ),
    FavorCreateSchema(
        name='Старт',
        includes=[
            'Мобильное приложение до 5 страниц',
            'Адаптивный дизайн',
            '1 месяц поддержки'
        ],
        duration_weeks=3,
        price=250000,
        application_type=prisma.models.enums.ApplicationType.MOBILE
    ),
    FavorCreateSchema(
        name='Бизнес',
        includes=[
            'Приложение магазин',
            'Платежные системы',
            'Личный кабинет',
            '3 месяца поддержки'
        ],
        duration_weeks=6,
        price=450000,
        application_type=prisma.models.enums.ApplicationType.MOBILE
    ),
    FavorCreateSchema(
        name='Премиум',
        includes=[
            'Высоконагруженные проекты',
            'Индивидуальная архитектура',
            'Сложные интеграции',
            '6 месяц поддержки'
        ],
        duration_weeks=8,
        price=700000,
        application_type=prisma.models.enums.ApplicationType.MOBILE
    ),

]


class SeedDataSchema(BaseModel):
    favor: list[FavorCreateSchema] = favors_data
