from unittest.mock import AsyncMock

import pytest


@pytest.fixture(scope="function")
def update_with_callback() -> AsyncMock:
    update = AsyncMock()
    update.callback_query = AsyncMock()
    return update


@pytest.fixture(scope="module")
def context_with_data():
    context = AsyncMock()
    context.user_data = {}
    return context
