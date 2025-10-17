from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

import uvicorn

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.on_event("startup")
def startup():
    ...

@app.get("/", response_class=HTMLResponse)
async def root():
    return ""

@app.post("/api/record")
async def record():
    # Здесь можно добавить логику записи в БД
    return {"status": 200, "message": "Данные сохранены"}
