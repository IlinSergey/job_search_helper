from datetime import datetime
from typing import Annotated

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column

import data_base.enums as enums
from data_base.db import Base

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]  # noqa: A003 VNE003
    user_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(length=50))
    last_name: Mapped[str] = mapped_column(String(length=50))
    username: Mapped[str] = mapped_column(String(length=100), nullable=False)
    chat_id: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[created_at]

    def __repr__(self):
        return f"User {self.username}, user_id {self.user_id}"


class SearchParams(Base):
    __tablename__ = "search_params"

    id: Mapped[intpk]  # noqa: A003 VNE003
    vacancy_name: Mapped[str] = mapped_column(String(length=120))
    experience: Mapped[enums.Experience]
    type_of_employment: Mapped[enums.Employment]
    schedule: Mapped[enums.Schedule]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id", ondelete='CASCADE'))

    def __repr__(self):
        return f"{self.vacancy_name}, {self.experience}, {self.type_of_employment}, {self.schedule}"


class Vacancy(Base):
    __tablename__ = "vacanciens"

    id: Mapped[intpk]  # noqa: A003 VNE003
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id", ondelete='CASCADE'))
    id_vacantion: Mapped[int] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(length=120), nullable=False)
    url: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    date_published: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    salary: Mapped[str] = mapped_column(String(length=30))
    is_showed: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self):
        return f"{self.name} ({self.salary})"


def create_tables() -> None:
    Base.metadata.create_all(bind=Base.engine)


if __name__ == "__main__":
    Base.metadata.create_all(bind=Base.engine)
