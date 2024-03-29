from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def covering_letter_keyboard(vacancy_id: int) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Cопроводительное письмо", callback_data=vacancy_id),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_subscribe_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Сопроводительное письмо доступно по подписке! \nПодписаться",
                                 callback_data="subscribe"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


START_KEYBOARD = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Заполнить анкету", callback_data="анкета")
        ]
    ])

EXPERIENCE_KEYBOARD = [
    [
        InlineKeyboardButton("Нет опыта", callback_data="noExperience"),
    ],
    [
        InlineKeyboardButton("От 1 года до 3 лет", callback_data="between1And3"),
    ],
    [
        InlineKeyboardButton("От 3 до 6 лет", callback_data="between3And6"),
    ],
    [
        InlineKeyboardButton("Более 6 лет", callback_data="moreThan6"),
    ],
]

EMPLOYMENT_KEYBOARD = [
    [
        InlineKeyboardButton("Полная занятость", callback_data="full"),
        InlineKeyboardButton("Частичная занятость", callback_data="part")
    ],
    [
        InlineKeyboardButton("Проектная работа", callback_data="project"),
        InlineKeyboardButton("Стажировка", callback_data="probation"),
    ],
]

SCHEDULE_KEYBOARD = [
    [
        InlineKeyboardButton("Удаленная работа", callback_data="remote"),
        InlineKeyboardButton("Полный день", callback_data="fullDay")
    ],
    [
        InlineKeyboardButton("Сменный график", callback_data="shift"),
        InlineKeyboardButton("Гибкий график", callback_data="flexible"),
    ],
]
