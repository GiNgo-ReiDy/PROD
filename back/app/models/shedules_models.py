from sqlmodel import Field, Relationship, SQLModel

class Schedules(SQLModel, table=True):
    id: int = Field(primary_key=True)
    group_id : int = Field(foreign_key='Groups.id')
    day: str
    begin : int
    end: int

