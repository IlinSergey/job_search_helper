from datetime import datetime

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        Text)
from sqlalchemy.orm import relationship

from data_base.db import Base, engine


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)  # noqa: A003, VNE003
    user_id = Column(Integer, unique=True, nullable=False)
    first_name = Column(String(length=50))
    last_name = Column(String(length=50))
    username = Column(String(length=100), nullable=False)
    chat_id = Column(Integer, nullable=False)
    vacancy = Column(Text)
    created_at = Column(DateTime, default=datetime.now())
    vacancies = relationship('Vacancy', back_populates='user')

    def __repr__(self):
        return f"User {self.username}, user_id {self.user_id}"


class Vacancy(Base):
    __tablename__ = 'vacanciens'

    id = Column(Integer, primary_key=True)  # noqa: A003, VNE003
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'))
    id_vacantion = Column(Integer, unique=True, nullable=False)
    name = Column(String(length=120), nullable=False)
    url = Column(String(50), nullable=False)
    description = Column(Text)
    date_published = Column(DateTime(timezone=True))
    salary = Column(String(length=30))
    is_showed = Column(Boolean, default=False)

    user = relationship('User', back_populates='vacancies')

    def __repr__(self):
        return f'{self.name} ({self.salary})'


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
