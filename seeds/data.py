import prisma
from pydantic import BaseModel

from api.favors.types.request import FavorSchema
from api.guarantees.types.request import GuaranteeSchema
from api.stages.types.request import StageSchema


favors_data = [
    FavorSchema(
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
    FavorSchema(
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
    FavorSchema(
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
    FavorSchema(
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
    FavorSchema(
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
    FavorSchema(
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

guarantees_data = [
    GuaranteeSchema(
        name='Возврат предоплаты при срыве сроков',
        image_url='https://s3-alpha-sig.figma.com/img/d843/2874/2c60563b3508d438307b06da1725732a?Expires=1735516800&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=RoBpIapBwAUME~Zt9qqbSQfj6PGNZKv6VqD16FQ5saXsdDyGHEMMcqzmOjY5~yiERq1BDWuM7d0Bp8opFsHSDcwc8zAbyKJhYJLaZL1OVHi16IZkjZB0pYjnBOZu00VT~RU-P6UvuIf0-7w9FVJjwdrD8ztgzLK0z-es5eCliS6pR3atedylZLcCuCrqBeY8eb07i2tzmBMjIfEPOLvg53Ah36KcuwAkUj3YlYLn3uhgPpS-Ewf9UYgMlL3S86Lpn4BJmbbv5Il7ogh6V7HtYbL5L~DCcSrbLK-5-ohddCuWMjgSWPEkx1sU6DivCZ53YDBpAZV~sASN1e-9Bk~7wA__'
    ),
    GuaranteeSchema(
        name='Бесплатное исправление багов',
        image_url='https://s3-alpha-sig.figma.com/img/8d09/092c/2dd8cb908c9ee4cd3e824a9f406770c4?Expires=1735516800&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=ZrGmObDOX3XrAJf1VpT04J8e2S-EeSqhjq~OS7Wzon7kru5xFI6d8rKJXx5vyKV42WFjvOidAsYa61XL3sx~6CTC8CPbCDa4TTGRVC26ncX~5kHtFTKRQCgclkJtQL02QzFaAGmJCuODQ9rDQGKpYrufxSZsVopxEmJ7YaH0TBUmAc9Id60ny2WOEjPPqRP2eUKBqODEFxOq2oUcFmM08B6inDadjSV7rXZenOTVEJag0kpUVbRNeOVxnXfFokj3YVQLKN2BGg5e-qCeqt9zqv77n7g7RIdsO~c6NMh9WoCooPidC4qucNxMN3UXNWeVrGssqgQLuDKzwoB5VZE0QA__'
    ),
    GuaranteeSchema(
        name='Поддержка в рабочее время',
        image_url='https://s3-alpha-sig.figma.com/img/13fd/af08/cb681b8c86e7ba38cf929e1d464c9649?Expires=1735516800&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=oPxLailmIyI9ExNT03q0MmMrVXxMqQRXemJff6k3O-bi-wpjJ2k4Plk9mgYlkNcUZNf4mQMdwfqzT05VmgO9mdg1KrM6bvCIEMRTJxeRCTjTayIdTJ8PGjvnst3~oacpnceHA49kH1cAhXZEsCnQ0MkC9QhEd8mUD-EBimE6G~N8~YZY6HV8lh3aNEAWJl0tK5e5W8HvbV2MFlhDN2qEnAZmTw0ieRydQ7WcoJ03fZ0D9Jf596VXRXxuK9u2VZFrrLxo5ElvWwtqezdWCjVX5IwRdTaZ-V2u5PexjEgbuXnQqaWc3Xy4diyFaC4VaI5AK6WZVHDwX2XmOc4WP-4LNw__'
    ),
    GuaranteeSchema(
        name='Документация по проекту',
        image_url='https://s3-alpha-sig.figma.com/img/4b1b/f36f/b26bf74ded3574186f5e7942a4d23e30?Expires=1735516800&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=DEG4SQWl3mRv9mzCxvPUJwSG31OcPxU5898uyXJMk-2Jitcuq9iCC8CyRU1Bw-PDkW26I60UTpa4hVUlxKEDhIRH5fJ29wnN4C8JikoyXYP-dP4MfjGWlN3i12JtyUb9KyOMzc4dE-TfwPRE7nPIUaiarr~2XwJ6oY~BESuCmdr6R-UTOu423Ug1-VwPuKy~eQJlDqzHjTaNyz-aQzqtMsQyNbdtCyVgU-i41cUsJ3kidcXIY~EWxeurkIp3uvXLA5KaXdH4-VA6~oYeSbEhwTZsfzOuIoWGWyEqsoLZtfD8zULXanfsbIFD2BH2N6l-1kIYhq47I0Ng7QWB8OeBEQ__'
    )
]

stages_data = [
    StageSchema(
        place=0,
        name='Обсуждение проекта',
        description='После того как вы отправите заявку или свяжитесь с нами, наш менеджер свяжется с вами в течение 24 часов для обсуждения всех деталей вашего проекта'
    ),
    StageSchema(
        place=1,
        name='Предоплата 30',
        description='После успешного обсуждения проекта и утверждения всех условий, мы переходим к этапу предоплаты. Предоплата необходима для начала работы над вашим проектом.'
    ),
    StageSchema(
        place=0,
        name='Обсуждение проекта',
        description='После того как вы отправите заявку или свяжитесь с нами, наш менеджер свяжется с вами в течение 24 часов для обсуждения всех деталей вашего проекта'
    ),
    StageSchema(
        place=0,
        name='Обсуждение проекта',
        description='После того как вы отправите заявку или свяжитесь с нами, наш менеджер свяжется с вами в течение 24 часов для обсуждения всех деталей вашего проекта'
    ),
    StageSchema(
        place=0,
        name='Обсуждение проекта',
        description='После того как вы отправите заявку или свяжитесь с нами, наш менеджер свяжется с вами в течение 24 часов для обсуждения всех деталей вашего проекта'
    ),
]


class SeedDataSchema(BaseModel):
    favor: list[FavorSchema] = favors_data
    guarantee: list[GuaranteeSchema] = guarantees_data
    stage: list[StageSchema] = stages_data
