from data_base.vacancy import is_vacancy_in_db, read_vacancy, record_vacancy


def test__record_vacancy(hh_vacancy, user_id):
    assert not is_vacancy_in_db(hh_vacancy["id_vacantion"])
    record_vacancy(hh_vacancy, user_id)
    assert is_vacancy_in_db(hh_vacancy["id_vacantion"])


class TestIsVacancyInDB:
    def test__is_vacancy_in_db(self, hh_vacancy):
        hh_vacancy["id_vacantion"] = 0
        assert not is_vacancy_in_db(hh_vacancy["id_vacantion"])

    def test__is_vacancy_in_db__vacancy_in_db(self, hh_vacancy):
        assert is_vacancy_in_db(hh_vacancy["id_vacantion"])


def test__read_vacancy(user_id):
    result = read_vacancy(user_id)
    assert result == ('Some description for test vacancy * https://hh.ru/vacancy/92292020', 92292020)
    assert read_vacancy(user_id) is None
