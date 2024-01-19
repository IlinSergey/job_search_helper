from datetime import datetime
from typing import TypedDict


class HHVacancy(TypedDict):
    id_vacantion: int
    name: str
    url: str
    descript: str
    date_published: datetime
    salary: str


class SearchParams(TypedDict):
    vacancy_name: str
    experience: str
    type_of_employment: str
    schedule: str
