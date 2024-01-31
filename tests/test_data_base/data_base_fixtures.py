from unittest.mock import Mock

import pytest
from sqlalchemy_utils import create_database, database_exists, drop_database

from data_base.db import Base
from data_base.models import SearchParams, User, Vacancy  # noqa: F401
from data_base.user import create_user
from utils.config import MODE


@pytest.fixture(scope="package")
def effective_user(user_id):
    effective_user = Mock()
    effective_user.id = user_id
    effective_user.first_name = "test name"
    effective_user.last_name = "test last name"
    effective_user.username = "test username"
    return effective_user


@pytest.fixture(scope="package", autouse=True)
def create_data_base_and_tables():
    assert MODE == "TEST"
    if not database_exists(Base.engine.url):
        create_database(Base.engine.url)
    Base.metadata.drop_all(Base.engine)
    Base.metadata.create_all(Base.engine)
    yield
    drop_database(Base.engine.url)


@pytest.fixture(scope="package", autouse=True)
def create_user_in_db(effective_user, chat_id):
    create_user(effective_user, chat_id)
