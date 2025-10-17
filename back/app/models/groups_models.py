from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users_models import User
    from .shedules_models import Schedule

class Group(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    group_name : str
    gpu_amount: int
    distribution: int
    hour_limitation: int

    schedules: list["Schedule"] = Relationship(back_populates="group")
    users: list["User"] = Relationship(back_populates="group")

    __tablename__ = 'groups'


class GroupPost(SQLModel):
    group_name : str
    gpu_amount: int
    distribution: int
    hour_limitation: int




