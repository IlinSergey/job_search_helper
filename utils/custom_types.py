from datetime import datetime
from typing import TypedDict


class HHVacancy(TypedDict):
    id_vacantion: int
    name: str
    url: str
    descript: str
    date_published: datetime
    salary: str

import requests

print(HHVacancy)

hh=HHVacancy()
