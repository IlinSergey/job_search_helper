from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker

from utils.config import DB


class Base(DeclarativeBase):
    engine = create_engine(url=DB)
    db_session = scoped_session(sessionmaker(bind=engine))
    query = db_session.query_property()
