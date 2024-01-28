from unittest.mock import patch

import responses

from bot import hh


class TestGetResponseHH:
    @responses.activate
    def test__get_response__hh_success(self, search_params, response_from_hh):
        responses.add(
            method=responses.GET,
            url="https://api.hh.ru/vacancies",
            json=response_from_hh,
            status=200
            )
        response = hh.get_response(search_params)
        assert response == response_from_hh

    @responses.activate
    def test__get_response__hh_error_400(self, search_params):
        responses.add(
            method=responses.GET,
            url="https://api.hh.ru/vacancies",
            status=400
            )
        response = hh.get_response(search_params)
        assert response is False

    @responses.activate
    def test__get_response__hh_error_429(self, search_params):
        responses.add(
            method=responses.GET,
            url="https://api.hh.ru/vacancies",
            status=429
            )
        response = hh.get_response(search_params)
        assert response is False

    @responses.activate
    def test__get_response__hh_error_555(self, search_params):
        responses.add(
            method=responses.GET,
            url="https://api.hh.ru/vacancies",
            status=555
            )
        response = hh.get_response(search_params)
        assert response is False


class TestFindVacationHH:
    def test__find_vacation__hh_success(self, search_params, user_id, response_from_hh):
        with (
            patch("bot.hh.get_response") as mock_get_response,
            patch("services.hh.record_vacancy") as mock_reord_vacancy
             ):
            mock_get_response.return_value = response_from_hh
            mock_reord_vacancy.return_value = None
            hh.find_vacation(search_params, user_id)
            assert mock_get_response.call_count == 1
            assert mock_reord_vacancy.call_count == 2

    def test__find_vacation__hh_not_response(self, search_params, user_id):
        with (
            patch("bot.hh.get_response") as mock_get_response,
            patch("services.hh.record_vacancy") as mock_reord_vacancy
             ):
            mock_get_response.return_value = False
            mock_reord_vacancy.return_value = None
            hh.find_vacation(search_params, user_id)
            assert mock_get_response.call_count == 1
            assert mock_reord_vacancy.call_count == 0


class TestGetDescriptionAboutVacation:
    @responses.activate
    def test__get_description_about_vacation__succes(self, vacation_id,
                                                     description_about_vacancy_response,
                                                     clear_vacancy_description):
        responses.add(
            method=responses.GET,
            url=f"https://api.hh.ru/vacancies/{vacation_id}",
            json=description_about_vacancy_response,
            status=200,
        )
        result = hh.get_description_about_vacation(vacation_id)
        assert result == clear_vacancy_description

    @responses.activate
    def test__get_description_about_vacation__error_404(self, vacation_id):
        responses.add(
            method=responses.GET,
            url=f"https://api.hh.ru/vacancies/{vacation_id}",
            status=404,
        )
        result = hh.get_description_about_vacation(vacation_id)
        assert result is False

    @responses.activate
    def test__get_description_about_vacation__error_555(self, vacation_id):
        responses.add(
            method=responses.GET,
            url=f"https://api.hh.ru/vacancies/{vacation_id}",
            status=555,
        )
        result = hh.get_description_about_vacation(vacation_id)
        assert result is False
