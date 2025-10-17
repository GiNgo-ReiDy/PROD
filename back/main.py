from fastapi.responses import HTMLResponse
from fastapi import FastAPI

from sqlmodel import SQLModel

from back.app.core import engine

import uvicorn

app = FastAPI()


@app.on_event("startup")
def strartup():
    SQLModel.metadata.create_all(bind=engine)


@app.get("/", response_class=HTMLResponse)
async def root():
    return "Hello world!"


uvicorn.run(app, host="0.0.0.0", port=8000)
