from unittest.mock import Mock, patch

import pytest

from services.jobs import send_vacation, update_db


class TestUpdateDB:
    @pytest.mark.asyncio
    async def test__update_db__succes(self, context, search_params, user_id):
        context._user_id = user_id
        with (
            patch("services.jobs.get_search_params") as mock_get_search_params,
            patch("services.jobs.hh.find_vacation") as mock_find_vacation,
             ):
            mock_get_search_params.return_value = search_params
            mock_find_vacation.return_value = None
            await update_db(context)
            assert mock_get_search_params.call_count == 1
            assert mock_find_vacation.call_count == 1

    @pytest.mark.asyncio
    async def test__update_db__not_user_id(self, context, user_id):
        context._user_id = user_id
        with (
            patch("services.jobs.get_search_params") as mock_get_search_params,
            patch("services.jobs.hh.find_vacation") as mock_find_vacation,
             ):
            mock_get_search_params.return_value = None
            await update_db(context)
            assert mock_get_search_params.call_count == 1
            assert mock_find_vacation.call_count == 0


class TestSendVacation:
    @pytest.mark.asyncio
    async def test__send_vacation__succes_without_subscribe(self, context, chat_id, user_id, vacancy_from_db):
        context._user_id = user_id
        context._chat_id = chat_id
        with (
            patch("services.jobs.read_vacancy") as mock_read_vacancy,
            patch("services.jobs.get_subscribe_keyboard") as mock_get_subscribe_keyboard,
              ):
            mock_read_vacancy.return_value = vacancy_from_db
            mocked_keyboard = Mock()
            mock_get_subscribe_keyboard.return_value = mocked_keyboard
            await send_vacation(context)
            assert mock_read_vacancy.call_count == 1
            context.bot.send_message.assert_called_with(
                chat_id=chat_id,
                text=vacancy_from_db[0],
                reply_markup=mocked_keyboard,
            )

    @pytest.mark.asyncio
    async def test__send_vacation__succes_with_keyboard(self, context, chat_id, vacancy_from_db):
        context._user_id = 1055229700
        context._chat_id = chat_id
        with (
            patch("services.jobs.read_vacancy") as mock_read_vacancy,
            patch("services.jobs.covering_letter_keyboard") as mock_covering_letter_keyboard,
              ):
            mock_read_vacancy.return_value = vacancy_from_db
            mocked_keyboard = Mock()
            mock_covering_letter_keyboard.return_value = mocked_keyboard
            await send_vacation(context)
            assert mock_read_vacancy.call_count == 1
            context.bot.send_message.assert_called_with(
                chat_id=chat_id,
                text=vacancy_from_db[0],
                reply_markup=mocked_keyboard,
            )

    @pytest.mark.asyncio
    async def test__send_vacation__not_vacancy_data(self, context, chat_id, user_id):
        context._user_id = user_id
        context._chat_id = chat_id
        with (
            patch("services.jobs.read_vacancy") as mock_read_vacancy,
            patch("services.jobs.covering_letter_keyboard") as mock_covering_letter_keyboard,
              ):
            mock_read_vacancy.return_value = None
            result = await send_vacation(context)
            assert result is None
            assert mock_covering_letter_keyboard.call_count == 0
            assert context.bot.send_message.call_count == 0
