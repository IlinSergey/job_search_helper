import logging
import re
from time import sleep
from typing import Any

import requests  # type: ignore

from data_base.vacancy import record_vacancy
from utils.custom_types import HHVacancy, SearchParams

logger = logging.getLogger(__name__)


class HHAgent:

    def get_response(self, search_params: SearchParams) -> dict[str, Any] | bool:
        url = "https://api.hh.ru/vacancies"
        params = {"User-Agent": "MyApp",
                  "text": search_params["vacancy_name"],
                  "experience": [search_params["experience"],],
                  "vacancy_search_fields": ["name"],
                  "resume_search_logic": "all",
                  "schedule": search_params["schedule"],
                  "employment": [search_params["type_of_employment"],],
                  "per_page": 100,
                  "period": 1,
                  }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            sleep(0.2)
            return False
        else:
            logger.warning(f"Не получили данных с HH! {params=}")
            return False

    def find_vacation(self, search_params: SearchParams, user_id: int) -> None:
        response = self.get_response(search_params)
        if response:
            for item in response["items"]:  # type: ignore[index]
                try:
                    if item["salary"] is not None:
                        salary = f'от {item["salary"].get("from", "Не указано")} до {item["salary"].get("to", "Не указано")}'  # noqa: E501
                        salary = salary.replace("None", "Не указано")
                    else:
                        salary = "Не указано"
                    description = (item["snippet"]["requirement"] + "\n"
                                   + item["snippet"]["responsibility"]).replace("<highlighttext>", "").replace("</highlighttext>", "")  # noqa: E501

                    vacancy = HHVacancy(
                        id_vacantion=int(item['id']),
                        name=item['name'],
                        url=item['alternate_url'],
                        descript=description,
                        date_published=item['published_at'],
                        salary=salary
                    )
                    record_vacancy(vacancy, user_id)
                except Exception:
                    continue

    def get_description_about_vacation(self, vacation_id: int) -> str | bool:
        url = f"https://api.hh.ru/vacancies/{vacation_id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            description = data["description"]
            description_text = re.sub(r"<[^>]+>", "", description, flags=re.S)
            return description_text
        else:
            logger.warning(F"Не получили детальное описание вакансии с id {vacation_id=}")
            return False
