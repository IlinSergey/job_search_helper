from unittest.mock import AsyncMock

import pytest
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot import start


@pytest.mark.asyncio
async def test__start_handler():
    update = AsyncMock()
    context = AsyncMock()

    keyboard = [
        [
            InlineKeyboardButton("Заполнить анкету", callback_data="анкета")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await start(update, context)

    update.message.reply_text.assert_called_with(f"Привет {update.effective_user.first_name},"
                                                 f" для успешного поиска вакансий, необходимо заполнить анкету",
                                                 reply_markup=reply_markup)
