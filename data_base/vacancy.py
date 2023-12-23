from utils.custom_types import HHVacancy

from data_base.db import db_session
from data_base.models import Vacancy


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
        db_session.add(data)
        db_session.commit()


def read_vacancy(user_id: int) -> tuple[str, int] | None:
    vacancy = Vacancy.query.filter((Vacancy.user_id == user_id) & (Vacancy.is_showed == False)).first()
    if vacancy:
        vacancy.is_showed = True
        db_session.commit()
        return (f'{vacancy.description} * {vacancy.url}', vacancy.id_vacantion)
    else:
        return None


def is_vacancy_in_db(vacancy_id: int) -> bool:
    '''
    Проверяем наличие вакансии в БД
    '''
    is_vacancy = Vacancy.query.filter(Vacancy.id_vacantion == vacancy_id).first()
    return bool(is_vacancy)
