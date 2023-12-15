import requests

from config import CATALOG_ID, YA_API_KEY


text = ''

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
            "text": "Ты опытный IT рекрутер."
        },
        {
            "role": "user",
            "text": "Привет, я хочу откликнуться на вакансию, напиши мне сопроводительное письмо к отклику?"
        },
        {
            "role": "assistant",
            "text": "Привет! Да, конечно я могу написать сопроводитедльное письмо для отклика, для этого мне нужно описание вакансии."
        },
        {
            "role": "user",
            "text": text
        }
    ]
}


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {YA_API_KEY}"
}

response = requests.post(url, headers=headers, json=prompt)
result = response.text
print(response.status_code)
pprint(result)