import json
import logging
import time

import requests  # type: ignore
import sentry_sdk

from utils.config import CATALOG_ID, SENTRY_DNS, YA_API_KEY

logger = logging.getLogger(__name__)

sentry_sdk.init(dsn=SENTRY_DNS, traces_sample_rate=1.0, profiles_sample_rate=1.0)


def get_covering_letter(vacancy_description: str) -> str:
    logger.info("Запрос к YaGPT")
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
    max_retries = 3
    delay_seconds = 1
    for _ in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=prompt)
        except Exception as e:
            logger.warning(f"Ошибка при запросе к YaGPT {e}")
            sentry_sdk.capture_exception(e)
            response = None
        if response is not None:
            match response.status_code:
                case 200:
                    json_result = json.loads(response.text)
                    letter = json_result["result"]["alternatives"][0]["message"]["text"].strip()
                    return letter
                case 429:
                    logger.warning(f"Повторяем запрос {response.status_code=}")
                    time.sleep(delay_seconds)
                case _:
                    logger.warning(f"Неизвестная ошибка при обращении к YaGPT {response.status_code}")
                    return f"Возникла ошибка {response.status_code}"
        return "Возникла ошибка при обращении к YaGPT"
    return "Произошла ошибка при обращении к YaGPT"
