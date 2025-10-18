from .routes import auth_router, users_router, groups_router, sessions_router
from fastapi import FastAPI, APIRouter


api_router = APIRouter(prefix='/api')

api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(groups_router)
api_router.include_router(sessions_router)