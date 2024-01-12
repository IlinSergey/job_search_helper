from unittest.mock import AsyncMock

import pytest

from bot import start
from utils.keyboards import start_keyboard


@pytest.mark.asyncio
async def test__start_handler():
    update = AsyncMock()
    context = AsyncMock()
    await start(update, context)
    update.message.reply_text.assert_called_with(f"Привет {update.effective_user.first_name},"
                                                 f" для успешного поиска вакансий, необходимо заполнить анкету",
                                                 reply_markup=start_keyboard)
