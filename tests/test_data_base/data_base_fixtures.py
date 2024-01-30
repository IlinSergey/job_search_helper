import pytest
from sqlalchemy_utils import create_database, database_exists, drop_database

from data_base.db import Base
from utils.config import MODE


@pytest.fixture(scope="session", autouse=True)
def create_tables():
    assert MODE == "TEST"
    engine = Base.engine
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.drop_all(Base.engine)
    Base.metadata.create_all(Base.engine)
    yield
    Base.metadata.drop_all(Base.engine)
    drop_database(engine.url)
