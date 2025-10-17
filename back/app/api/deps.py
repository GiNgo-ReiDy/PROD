from fastapi import Depends, FastAPI, HTTPException
from back.app.core import engine
from sqlmodel import Session
from typing import Annotated

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
