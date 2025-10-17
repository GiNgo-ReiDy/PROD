from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class Session(SQLModel):
    user_uuid: str = Field(foreign_key="users.uuid")
    start_time: str
    break_time: str
    stop_time: str | None = Field(default=None)

