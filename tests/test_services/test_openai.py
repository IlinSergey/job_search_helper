import responses

from services.openai import get_covering_letter


@responses.activate
def test__get_covering_letter__success(covering_letter_from_openai_response):
    responses.add(
        method=responses.POST,
        url="https://api.openai.com/v1/completions",
        json=covering_letter_from_openai_response,
        status=200
    )
    vacancy_description = "test description"
    result = get_covering_letter(vacancy_description)
    assert result == "Test covering letter from OpenAI service"


@responses.activate
def test__get_covering_letter__error_401():
    responses.add(
        method=responses.POST,
        url="https://api.openai.com/v1/completions",
        status=401
    )
    vacancy_description = "test description"
    result = get_covering_letter(vacancy_description)
    assert result == "Возникла ошибка, мы уже разбираемся"


@responses.activate
def test__get_covering_letter__error_429():
    responses.add(
        method=responses.POST,
        url="https://api.openai.com/v1/completions",
        status=429
    )
    vacancy_description = "test description"
    result = get_covering_letter(vacancy_description)
    assert result == "Возникла ошибка при обращении к OpenAI"


@responses.activate
def test__get_covering_letter__error_500():
    responses.add(
        method=responses.POST,
        url="https://api.openai.com/v1/completions",
        status=500
    )
    vacancy_description = "test description"
    result = get_covering_letter(vacancy_description)
    assert result == "Возникла ошибка при обращении к OpenAI"


@responses.activate
def test__get_covering_letter__error_503():
    responses.add(
        method=responses.POST,
        url="https://api.openai.com/v1/completions",
        status=503
    )
    vacancy_description = "test description"
    result = get_covering_letter(vacancy_description)
    assert result == "Возникла ошибка при обращении к OpenAI"


@responses.activate
def test__get_covering_letter__error_555():
    responses.add(
        method=responses.POST,
        url="https://api.openai.com/v1/completions",
        status=555
    )
    vacancy_description = "test description"
    result = get_covering_letter(vacancy_description)
    assert result == "Возникла ошибка 555"
