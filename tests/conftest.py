from unittest.mock import AsyncMock

import pytest


@pytest.fixture(scope="session")
def update() -> AsyncMock:
    return AsyncMock()


@pytest.fixture(scope="session")
def context() -> AsyncMock:
    return AsyncMock()
