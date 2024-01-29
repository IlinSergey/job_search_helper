import logging
import time

import requests  # type: ignore

from utils.config import OPEN_AI_KEY

API_KEY = OPEN_AI_KEY
MODEL = "text-davinci-003"

logger = logging.getLogger(__name__)


def get_covering_letter(vacancy_description: str) -> str:
    prompt = f"Напиши сопроводительное письмо для отклика на следующую вакансию: {vacancy_description}"
    max_retries = 3
    delay_seconds = 1
    for _ in range(max_retries):
        try:
            response = requests.post(
                "https://api.openai.com/v1/completions",
                headers={"Authorization": f"Bearer {API_KEY}"},
                json={"model": MODEL, "prompt": prompt, "temperature": 0.4, "max_tokens": 2000}
            )
        except Exception as e:
            logger.warning(f"Ошибка при запросе к OpenAI {e}")
            response = None
        if response is not None:
            match response.status_code:
                case 200:
                    result = response.json()
                    final_result = "".join(choice["text"] for choice in result["choices"])
                    return final_result
                case 401:
                    logger.warning("Поблемы с API ключом OpenAI!")
                    return "Возникла ошибка, мы уже разбираемся"
                case 429 | 500 | 503:
                    logger.warning(f"Повторяем запрос {response.status_code=}")
                    time.sleep(delay_seconds)
                case _:
                    logger.warning(f"Неизвестная ошибка при обращении к OpenAI {response.status_code}")
                    return f"Возникла ошибка {response.status_code}"
        return "Возникла ошибка при обращении к OpenAI"
    return "Возникла ошибка при обращении к OpenAI"
