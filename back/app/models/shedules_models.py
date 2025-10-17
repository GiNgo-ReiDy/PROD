from sqlmodel import Field, Relationship, SQLModel
from .groups_models import Group


class Schedule(SQLModel, table=True):
    id: int = Field(primary_key=True)
    group_id : int = Field(foreign_key='groups.id')
    day: str
    begin : int
    end: int

    group: Group = Relationship(back_populates="users")

    __tablename__ = 'schedules'

