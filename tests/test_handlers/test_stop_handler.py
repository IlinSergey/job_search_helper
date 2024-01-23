from unittest.mock import Mock

import pytest

from bot import stop


@pytest.mark.asyncio
async def test__stop_handler__with_job(update, context):
    jobs = [Mock(), Mock(), Mock()]
    context.job_queue.jobs = Mock(return_value=jobs)
    await stop(update, context)
    assert context.job_queue.jobs.call_count == 1
    update.message.reply_text.assert_called_with("Автоматический поиск остановлен")
    job_remove_count = 0
    for job in jobs:
        job_remove_count += 1
        job.schedule_removal.assert_called()
    assert job_remove_count == len(jobs)


@pytest.mark.asyncio
async def test__stop_handler__without_job(update, context):
    context.job_queue.jobs = Mock(return_value=None)
    await stop(update, context)
    assert context.job_queue.jobs.call_count == 1
    update.message.reply_text.assert_called_with("Ничего не запущено")
