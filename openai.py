import requests

from config import OPEN_AI_KEY

API_KEY = OPEN_AI_KEY
MODEL = "text-davinci-003"


def openai_request(user_input: str):
    prompt = user_input
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
        return "Возникла ошибка"
