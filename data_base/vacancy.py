from db import db_session
from models import Vacancy

from custom_types import HHVacancy


def record_vacation(vacancy: HHVacancy, user_id: int):
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
