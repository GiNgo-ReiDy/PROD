from sqlmodel import SQLModel, Field, Relationship
from uuid import uuid4


class BaseUser(SQLModel):
    login: str = Field(unique=True)


class User(BaseUser, table=True):
    uuid: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    password_hash: bytes
    group_id: int = Field(foreign_key="groups.id")
    category: int

    group: "Group" = Relationship(back_populates="users")
    session: "Session" = Relationship(back_populates='user')

    __tablename__ = "users"


class UserGet(BaseUser):
    ...

