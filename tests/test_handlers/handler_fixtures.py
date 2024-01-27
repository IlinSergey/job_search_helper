from unittest.mock import AsyncMock

import pytest


@pytest.fixture(scope="function")
def update() -> AsyncMock:
    return AsyncMock()


@pytest.fixture(scope="function")
def context() -> AsyncMock:
    return AsyncMock()
