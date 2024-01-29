from unittest.mock import patch

import pytest
from telegram import InlineKeyboardMarkup

from utils import keyboards
from utils.anketa import (anketa_start, save_employment, save_experience,
                          save_schedule, save_vacancy)


@pytest.mark.asyncio
async def test__anketa_start_handler(update_with_callback, context):
    result = await anketa_start(update_with_callback, context)
    assert result == "vacancy_name"
    update_with_callback.callback_query.edit_message_text.assert_called_with("Введите текст для поиска вакансии:")


@pytest.mark.asyncio
async def test__save_vacancy_handler(update, context_with_data):
    update.message.text = "test"
    result = await save_vacancy(update, context_with_data)
    assert result == "experience"
    assert context_with_data.user_data["vacancy_name"] == "test"
    reply_markup = InlineKeyboardMarkup(keyboards.EXPERIENCE_KEYBOARD)
    update.message.reply_text.assert_called_with("Выбери опыт работы:", reply_markup=reply_markup)


@pytest.mark.asyncio
async def test__save_experience_handler(update_with_callback, context_with_data):
    update_with_callback.callback_query.data = "test experience"
    result = await save_experience(update_with_callback, context_with_data)
    assert result == "type_of_employment"
    assert context_with_data.user_data["experience"] == "test experience"
    reply_markup = InlineKeyboardMarkup(keyboards.EMPLOYMENT_KEYBOARD)
    update_with_callback.callback_query.edit_message_text.assert_called_with(
        "Выбери тип занятости:", reply_markup=reply_markup
        )


@pytest.mark.asyncio
async def test__save_employment_handler(update_with_callback, context_with_data):
    update_with_callback.callback_query.data = "test employment"
    result = await save_employment(update_with_callback, context_with_data)
    assert result == "schedule"
    assert context_with_data.user_data["type_of_employment"] == "test employment"
    reply_markup = InlineKeyboardMarkup(keyboards.SCHEDULE_KEYBOARD)
    update_with_callback.callback_query.edit_message_text.assert_called_with(
        "Выбери график работы:", reply_markup=reply_markup
        )


@pytest.mark.asyncio
async def test__save_schedule_handler(update_with_callback, context_with_data):
    with patch("utils.anketa.create_search_params") as mock_create_search_params:
        mock_create_search_params.return_value = None
        update_with_callback.callback_query.data = "test schedule"
        result = await save_schedule(update_with_callback, context_with_data)
        update_with_callback.callback_query.edit_message_text.assert_called_with(
            "Данные для поиска сохранены!"
            )
        assert result == -1
        assert mock_create_search_params.call_count == 1
