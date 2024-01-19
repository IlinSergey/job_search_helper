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
    try:
        search_params = Base.db_session.get(SearchParams, user_id)
        search_params.vacancy_name = params.vacancy_name  # type: ignore [attr-defined]
        search_params.experience = params.experience  # type: ignore [attr-defined]
        search_params.type_of_employment = params.type_of_employment  # type: ignore [attr-defined]
        search_params.schedule = params.schedule  # type: ignore [attr-defined]
    except NoResultFound:
        Base.db_session.add(params)
    Base.db_session.commit()
