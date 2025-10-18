from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel
from uuid import uuid4

from .groups_models import Group, GroupGetWithUsers, GroupGet
from .sessions_models import Session, SessionGet


class UserBase(SQLModel):
    login: str
    category: int


class User(UserBase, table=True):
    uuid: str | None = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    group_id: int | None = Field(default=None, foreign_key="groups.id")
    password_hash: bytes

    group: Group | None = Relationship(back_populates="users")
    session: Session | None = Relationship(back_populates="user")

    __tablename__ = 'users'


class UserGet(UserBase):
    uuid: str
    session: SessionGet | None = None


class UserGetWithGroup(UserGet):
    group: GroupGet | None = None


class UserPost(UserBase):
    password: str
    group_id: int | None = None


class UserPatch(BaseModel):
    uuid: str
    login: str | None = None
    password: str | None = None
    group_id: int | None = None
    category: int | None = None



GroupGetWithUsers.model_rebuild()