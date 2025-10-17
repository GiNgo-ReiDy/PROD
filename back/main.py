from fastapi.responses import HTMLResponse
from fastapi import FastAPI

import uvicorn

app = FastAPI()


app.on_event("startup")
def strartup():
    ...


@app.get("/", response_class=HTMLResponse)
async def root():
    return "Hello world!"
