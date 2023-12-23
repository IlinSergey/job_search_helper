import json

import requests  # type: ignore

from utils.config import CATALOG_ID, YA_API_KEY


def get_covering_letter(vacancy_description: str) -> str:
    prompt = {
        "modelUri": f"gpt://{CATALOG_ID}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты опытный IT рекрутер. Твоя задача, на основе описания вакансии составить тект отклика"
            },
            {
                "role": "user",
                "text": "Напиши отклик на вакансию"
            },
            {
                "role": "assistant",
                "text": "Конечно я могу написать текст для отклика на вакансию, для этого мне нужно описание вакансии."
            },
            {
                "role": "user",
                "text": vacancy_description
            }
        ]
    }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {YA_API_KEY}"
    }

    response = requests.post(url, headers=headers, json=prompt)
    if response.status_code == 200:
        json_result = json.loads(response.text)
        letter = json_result['result']['alternatives'][0]['message']['text'].strip()
        return letter
    return f'Произошла ошибка {response.status_code}'
