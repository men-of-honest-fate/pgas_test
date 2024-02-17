from __future__ import annotations

from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime
from sqlalchemy import Enum as DbEnum
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Kind(str, Enum):
    ORAL: str = "oral"
    POSTER: str = "poster"
    INVITED: str = "invited"
    PLENAR: str = "plenar"


class Presentation(Base):
    __tablename__ = "presentations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    conference: Mapped[str] = mapped_column(String)
    publicationDate: Mapped[str] = mapped_column(String)
    start: Mapped[datetime] = mapped_column(DateTime)
    end: Mapped[datetime] = mapped_column(DateTime)
    place: Mapped[str] = mapped_column(String, nullable=True)
    kind: Mapped[Kind] = mapped_column(DbEnum(Kind, native_enum=False), nullable=False)
    presentationid: Mapped[int] = mapped_column(String, unique=True)
    confid: Mapped[int] = mapped_column(Integer)
    created: Mapped[datetime] = mapped_column(DateTime)

    users: Mapped[list[User]] = relationship(
        "User", secondary="presentations_users", back_populates="presentations"
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    irid: Mapped[int] = mapped_column(Integer, unique=True)
    name: Mapped[str] = mapped_column(String)

    presentations: Mapped[list[Presentation]] = relationship(
        "Presentation", secondary="presentations_users", back_populates="users"
    )


class PresUser(Base):
    __tablename__ = "presentations_users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey("presentations.id"))