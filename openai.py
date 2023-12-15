import requests

from config import OPEN_AI_KEY

API_KEY = OPEN_AI_KEY
MODEL = "text-davinci-003"


def get_covering_letter(vacancy_description: str) -> str:
    prompt = f"Напиши сопроводительное письмо для отклика на следующую вакансию: {vacancy_description}"
    try:
        response = requests.post(
            "https://api.openai.com/v1/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"model": MODEL, "prompt": prompt, "temperature": 0.4, "max_tokens": 2000}
        )
    except Exception:
        response = False
    if response:
        result = response.json()
        final_result = "".join(choice["text"] for choice in result["choices"])
        return final_result
    else:
        print(response.status_code)
        return "Возникла ошибка"
