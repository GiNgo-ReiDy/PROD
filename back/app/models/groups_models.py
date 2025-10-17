from sqlmodel import Field, Relationship, SQLModel
from .shedules_models import Schedule, ScheduleGet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users_models import User, UserGet


class GroupBase(SQLModel):
    group_name: str
    gpu_amount: int
    distribution: int
    hour_limitation: int


class Group(GroupBase, table=True):
    id: int | None = Field(primary_key=True, default=None)
    schedules: list["Schedule"] = Relationship(back_populates="group")
    users: list["User"] = Relationship(back_populates="group")

    __tablename__ = 'groups'


class GroupGet(GroupBase):
    id: int
    schedules: list[ScheduleGet]


class GroupGetWithUsers(GroupGet):
    users: list["UserGet"]


class GroupPost(GroupBase):
    pass




