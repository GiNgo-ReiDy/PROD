from sqlmodel import Field, Relationship, SQLModel
from .schedules_models import Schedules

class Groups(SQLModel, table=True):
    id: int = Field(primary_key=True)
    group_name : str
    gpu_amount: int
    distribution: int
    hour_limitation: int
    schedule_limitation: list[Schedules] = Relationship()


