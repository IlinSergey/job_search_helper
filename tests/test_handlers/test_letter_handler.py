from unittest.mock import patch

import pytest

from bot import letter


@pytest.mark.asyncio
async def test__letter_handler(update, context):
    with (patch("bot.hh.get_description_about_vacation") as mock_get_description_about_vacation,
          patch("bot.get_covering_letter") as mock_get_covering_letter,
          ):
        mock_get_description_about_vacation.return_value = "test description"
        mock_get_covering_letter.return_value = "covering letter for test description"
        await letter(update, context)
        update.callback_query.message.reply_text.assert_called_with("covering letter for test description")
        assert update.callback_query.message.reply_text.call_count == 2


@pytest.mark.asyncio
async def test__letter_handler__vacancy_id_is_none(update, context):
    update.callback_query.data = None
    await letter(update, context)
    assert update.callback_query.message.reply_text.call_count == 1
    update.callback_query.message.reply_text.assert_called_with(
        "Готовим сопроводительное письмо, это займет какое-то время..."
        )
