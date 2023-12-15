import re

import requests

from data_base import read_vacantion, record_vacation


class HHAgent:

    def get_response(self, vacancy_name):
        url = "https://api.hh.ru/vacancies"
        params = {"User-Agent": "MyApp",
                  "text": f"{vacancy_name} NOT Аналитик NOT Devops NOT DevOps NOT Менеджер NOT Data NOT Инженер NOT Преподаватель",
                  "experience": ["noExperience", "between1And3"],
                  "vacancy_search_fields": ["name"],
                  "resume_search_logic": "all",
                  "schedule": "remote",
                  "per_page": 100,
                  "period": 1,
                  }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return False

    def find_vacation(self, vacancy_name, user_id):
        response = self.get_response(vacancy_name)
        if response:
            for item in response["items"]:
                try:
                    if item["salary"] != "None":
                        salary = f'от {item["salary"].get("from", "Не указано")} до {item["salary"].get("to", "Не указано")}'
                        salary = salary.replace("None", "Не указано")
                    else:
                        salary = "Не указано"
                    description = (item["snippet"]["requirement"] + "\n"
                                   + item["snippet"]["responsibility"]).replace("<highlighttext>", "").replace("</highlighttext>", "")
                    record_vacation(int(item["id"]), item["name"], item["alternate_url"],
                                    description, item["published_at"], salary, user_id)
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
