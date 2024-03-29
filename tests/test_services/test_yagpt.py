import responses

from services.yagpt import get_covering_letter


@responses.activate
def test__get_covering_letter__success(covering_letter_from_yagpt_response):
    responses.add(
        method=responses.POST,
        url="https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
        json=covering_letter_from_yagpt_response,
        status=200
    )
    vacancy_description = "test description"
    result = get_covering_letter(vacancy_description)
    assert result == "covering letter for test description."


@responses.activate
def test__get_covering_letter__error_429():
    responses.add(
        method=responses.POST,
        url="https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
        status=429
    )
    vacancy_description = "test description"
    result = get_covering_letter(vacancy_description)
    assert result == "Возникла ошибка при обращении к YaGPT"


@responses.activate
def test__get_covering_letter__error_555():
    responses.add(
        method=responses.POST,
        url="https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
        status=555
    )
    vacancy_description = "test description"
    result = get_covering_letter(vacancy_description)
    assert result == "Возникла ошибка 555"
