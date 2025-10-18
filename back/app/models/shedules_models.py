from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .groups_models import Group


class BaseSchedule(SQLModel):
    day: str
    begin: int
    end: int


class Schedule(BaseSchedule, table=True):
    id: int = Field(primary_key=True)
    group_id : int = Field(foreign_key='groups.id')


    group: "Group" = Relationship(back_populates="schedules")

    __tablename__ = 'schedules'


class ScheduleGet(BaseSchedule):
    pass


class SchedulePost(BaseSchedule):
    group_id: int