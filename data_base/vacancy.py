from db import db_session
from models import Vacancy

from custom_types import HHVacancy


def record_vacancy(vacancy: HHVacancy, user_id: int) -> None:
    if not is_vacancy_in_db(vacancy['id_vacantion']):
        data = Vacancy(
            id_vacantion=vacancy['id_vacantion'],
            name=vacancy['name'],
            url=vacancy['url'],
            descript=vacancy['descript'],
            date_published=vacancy['date_published'],
            salary=vacancy['salary'],
            user_id=user_id,
        )
        db_session.add(data)
        db_session.commit()


def read_vacancy(user_id: int) -> str | None:
    vacancy = Vacancy.query.filter(user_id=user_id,
                                   is_showed=False).order_by(Vacancy.date_published).first()
    if vacancy:
        vacancy.is_showed = True
        db_session.commit()
        return f'{vacancy.description} * {vacancy.url}'


def is_vacancy_in_db(vacancy_id: int) -> bool:
    '''
    Проверяем наличие вакансии в БД
    '''
    is_vacancy = Vacancy.query.filter(id_vacantion=vacancy_id).first()
    return bool(is_vacancy)
