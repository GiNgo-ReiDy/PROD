from sqlmodel import SQLModel, Field, Relationship
from uuid import uuid4

from .groups_models import Group, GroupGetWithUsers, GroupGet
from .sessions_models import Session, SessionGet


class BaseUser(SQLModel):
    login: str
    category: int


class User(BaseUser, table=True):
    uuid: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    group_id: int = Field(default=None, foreign_key="groups.id")
    password_hash: bytes

    group: Group = Relationship(back_populates="users")
    session: Session | None = Relationship(back_populates="user")

    __tablename__ = 'users'


class UserGet(BaseUser):
    uuid: str
    session: SessionGet


class UserGetWithGroup(UserGet):
    group: GroupGet


GroupGetWithUsers.model_rebuild()