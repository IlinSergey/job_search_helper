from sqlalchemy.orm.exc import NoResultFound

from data_base.db import Base
from data_base.models import SearchParams
from utils.custom_types import SearchParams as SearchParamsType


def create_search_params(user_id: int, search_params: SearchParamsType) -> None:
    params = SearchParams(
        vacancy_name=search_params['vacancy_name'],
        experience=search_params['experience'],
        type_of_employment=search_params['type_of_employment'],
        schedule=search_params['schedule'],
        user_id=user_id
    )
    search_params_in_db: SearchParams | None = Base.db_session.get(SearchParams, user_id)
    if search_params_in_db is not None:
        search_params_in_db.vacancy_name = params.vacancy_name
        search_params_in_db.experience = params.experience
        search_params_in_db.type_of_employment = params.type_of_employment
        search_params_in_db.schedule = params.schedule
    else:
        Base.db_session.add(params)
    Base.db_session.commit()


def get_search_params(user_id: int) -> SearchParamsType | None:
    try:
        search_params = Base.db_session.get_one(SearchParams, user_id)
        result = SearchParamsType(
            vacancy_name=search_params.vacancy_name,
            experience=search_params.experience.value,
            type_of_employment=search_params.type_of_employment.value,
            schedule=search_params.schedule.value,
        )
        return result
    except NoResultFound:
        return None
