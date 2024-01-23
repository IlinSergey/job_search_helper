from unittest.mock import AsyncMock

import pytest

from bot import run


@pytest.mark.asyncio
async def test__run_handler__reply_text(update, context):
    await run(update, context)
    update.message.reply_text.assert_called_with("Начинаем периодический поиск и рассылку подходящих вакансий")


@pytest.mark.asyncio
async def test__run_handler__jobs_run(update, context):
    context.job_queue.run_repeating = AsyncMock()
    await run(update, context)
    assert context.job_queue.run_repeating.call_count == 2
