from datetime import datetime

from sqlalchemy import (Boolean, Column, CheckConstraint, DateTime,
                        ForeignKey, Integer, String, Text)
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
    created_at = Column(DateTime, default=datetime.now())
    vacancies = relationship('Vacancy', back_populates='user')

    def __repr__(self):
        return f"User {self.username}, user_id {self.user_id}"


class SearchParams(Base):
    __tablename__ = 'search_params'

    vacancy_name = Column(Text)
    experience = Column(String(length=20))
    type_of_employment = Column(String(length=20))
    schedule = Column(String(length=20))

    __table_args__ = (
        CheckConstraint(
            experience.in_(['noExperience', 'between1And3', 'between3And6', 'moreThan6']) &
            type_of_employment.in_(['full', 'part', 'project', 'probation']) &
            schedule.in_(['fullDay', 'shift', 'remote', 'flexible']),
            name='check_constraints'),
    )


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
