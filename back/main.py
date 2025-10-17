from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from sqlmodel import SQLModel

from back.app.core import engine
from back.app.api import api_router

import uvicorn


app = FastAPI()
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def strartup():
    SQLModel.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
async def root():
    return ""

@app.post("/api/record")
async def record():
    # Здесь можно добавить логику записи в БД
    return {"status": 200, "message": "Данные сохранены"}
