from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from sqlmodel import SQLModel, Session, select

from back.app.core.security import hash_password
from back.app.models.users_models import User
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
async def strartup():
    SQLModel.metadata.create_all(bind=engine)

    with Session(engine) as session:
        # noinspection PyTypeChecker
        admin = session.exec(select(User).where(User.category == 2)).first()
        if not admin:
            admin = User(login="Root", category=2, password_hash=hash_password("root"))
            session.add(admin)
            session.commit()

@app.get("/", response_class=HTMLResponse)
async def root():
    return ""

@app.post("/api/record")
async def record():
    # Здесь можно добавить логику записи в БД
    return {"status": 200, "message": "Данные сохранены"}

uvicorn.run(app, host="127.0.0.1", port=8000)
