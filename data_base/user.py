from telegram import User as tg_user

from data_base.db import Base
from data_base.models import User


def create_user(effective_user: tg_user, chat_id: int) -> None:
    user = User(
        user_id=effective_user.id,
        first_name=effective_user.first_name,
        last_name=effective_user.last_name,
        username=effective_user.username,
        chat_id=chat_id,
    )
    Base.db_session.add(user)
    Base.db_session.commit()


def set_vacancy(effective_user: tg_user, vacany_name: str) -> None:
    """
    Устанавливает название вакансии для поиска
    vacancy_name: название по которому будет осуществляться поиск вакансий
    """
    user = User.query.filter(User.user_id == effective_user.id).first()
    user.vacancy = vacany_name
    Base.db_session.commit()


def is_user_in_db(effective_user: tg_user) -> bool:
    """
    Проверяет, есть ли текущий пользователь в БД
    """
    is_user = User.query.filter(User.user_id == effective_user.id).first()
    return bool(is_user)


def find_vacancy_name(user_id: int) -> str | None:
    user = User.query.filter(User.user_id == user_id).first()
    return user.vacancy
