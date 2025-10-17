from sqlmodel import SQLModel, Field, Relationship
from typing import Union
from uuid import uuid4

from .groups_models import Group
from .sessions_models import Session


class User(SQLModel, table=True):
    uuid: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    group_id: int = Field(default=None, foreign_key="groups.id")
    login: str
    password_hash: bytes
    category: int

    group: "Group" = Relationship(back_populates="users")
    session: Union["Session", None] = Relationship(back_populates="user")
