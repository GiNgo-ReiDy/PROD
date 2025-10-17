from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .users_models import User


class Session(SQLModel, table=True):
    user_uuid: str = Field(foreign_key="users.uuid", primary_key=True)
    start_time: str
    break_time: str
    stop_time: str | None = Field(default=None)

    user: "User" = Relationship(back_populates="session")


class SessionGet(SQLModel):
    start_time: str
    break_time: str
    stop_time: str | None = Field(default=None)