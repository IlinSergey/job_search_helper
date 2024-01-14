import logging

import requests  # type: ignore

from utils.config import OPEN_AI_KEY

API_KEY = OPEN_AI_KEY
MODEL = "text-davinci-003"

logger = logging.getLogger(__name__)


def get_covering_letter(vacancy_description: str) -> str:
    prompt = f"Напиши сопроводительное письмо для отклика на следующую вакансию: {vacancy_description}"
    try:
        response = requests.post(
            "https://api.openai.com/v1/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"model": MODEL, "prompt": prompt, "temperature": 0.4, "max_tokens": 2000}
        )
    except Exception as e:
        logger.warning(f"Ошибка при запросе к OpenAI {e}")
        response = False
    if response:
        result = response.json()
        final_result = "".join(choice["text"] for choice in result["choices"])
        return final_result
    else:
        logger.warning(f"Ошибка при обращении к OpenAI {response.status_code}")
        return f"Возникла ошибка {response.status_code}"
