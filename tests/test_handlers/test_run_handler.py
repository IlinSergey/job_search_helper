from unittest.mock import AsyncMock

import pytest

from bot import run


@pytest.mark.asyncio
async def test__run_handler__reply_text(update: AsyncMock, context: AsyncMock):
    await run(update, context)
    update.message.reply_text.assert_called_with("Начинаем периодический поиск и рассылку подходящих вакансий")


@pytest.mark.asyncio
async def test__run_handler__jobs_run(update: AsyncMock, context: AsyncMock):
    context.job_queue.run_repeating = AsyncMock()
    await run(update, context)
    assert len(context.job_queue.run_repeating.mock_calls) == 2
