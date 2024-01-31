from functools import cache

from data_base.db import Base
from data_base.models import Vacancy
from utils.custom_types import HHVacancy


def record_vacancy(vacancy: HHVacancy, user_id: int) -> None:
    if not is_vacancy_in_db(vacancy['id_vacantion']):
        data = Vacancy(
            id_vacantion=vacancy['id_vacantion'],
            name=vacancy['name'],
            url=vacancy['url'],
            description=vacancy['descript'],
            date_published=vacancy['date_published'],
            salary=vacancy['salary'],
            user_id=user_id,
        )
        Base.db_session.add(data)
        Base.db_session.commit()


def read_vacancy(user_id: int) -> tuple[str, int] | None:
    vacancy = Vacancy.query.filter((Vacancy.user_id == user_id) & (Vacancy.is_showed == False)).first()  # noqa: E712
    if vacancy:
        vacancy.is_showed = True
        Base.db_session.commit()
        return (f'{vacancy.description} * {vacancy.url}', vacancy.id_vacantion)
    else:
        return None


@cache
def is_vacancy_in_db(vacancy_id: int) -> bool:
    '''
    Проверяем наличие вакансии в БД
    '''
    is_vacancy = Vacancy.query.filter(Vacancy.id_vacantion == vacancy_id).first()
    return bool(is_vacancy)
