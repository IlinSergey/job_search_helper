import responses

from services.openai import get_covering_letter


@responses.activate
def test__get_covering_letter__success(covering_letter_from_openai_response):
    responses.add(
        method=responses.POST,
        url="https://api.openai.com/v1/completions",
        json=covering_letter_from_openai_response
    )
    vacancy_description = "test description"
    result = get_covering_letter(vacancy_description)
    assert result == "Test covering letter from OpenAI service"


@responses.activate
def test__get_covering_letter__error():
    responses.add(
        method=responses.POST,
        url="https://api.openai.com/v1/completions",
        status=500
    )
    vacancy_description = "test description"
    result = get_covering_letter(vacancy_description)
    assert result == "Возникла ошибка 500"
