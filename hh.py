import re

import requests

from data_base import record_vacation, read_vacantion


class HHAgent:

    def get_response(self):
        url = "https://api.hh.ru/vacancies"
        params = {"User-Agent": "MyApp",
                  "text": "Python",
                  "experience": ["noExperience", "between1And3"],
                  "vacancy_search_fields": ["name"],
                  "professional_role": "96",
                  "resume_search_logic": "all",
                  "schedule": "remote",
                  "per_page": 100,
                  "period": 10,
                  }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return False

    def find_vacation(self):
        response = self.get_response()
        if response:
            for item in response["items"]:
                try:
                    if item["salary"] != "None":
                        salary = f'от {item["salary"].get("from", "Не указано")} до {item["salary"].get("to", "Не указано")}'
                    else:
                        salary = "Не указано"
                    description = (item["snippet"]["requirement"] + "\n"
                                   + item["snippet"]["responsibility"]).replace("<highlighttext>", "").replace("</highlighttext>", "")
                    record_vacation(int(item["id"]), item["name"], item["alternate_url"],
                                    description, item["published_at"], salary)
                except Exception:
                    continue

    def get_vacantion(self):
        return read_vacantion()

    def get_description_about_vacation(self, vacation_id: int):
        url = f"https://api.hh.ru/vacancies/{vacation_id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            description = data["description"]
            description_text = re.sub(r"<[^>]+>", "", description, flags=re.S)
            return description_text
        else:
            return False
