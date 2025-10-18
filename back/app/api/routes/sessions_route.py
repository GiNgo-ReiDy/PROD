from typing import Annotated

from back.app.models.groups_models import Group, GroupPost, GroupGetWithUsers, GroupPatch
from fastapi import APIRouter, HTTPException, Depends, Body
from back.app.api.deps import SessionDep, AdminDep
from sqlmodel import select

process_running = False

router = APIRouter(prefix = '/sessions')
@router.post('/start-session')
async def start_session(session: SessionDep = Depends(SessionDep)):
    global process_running
    if process_running:
        raise HTTPException(status_code = 409) #типо конфликт с текущим состоянием сервера
    process_running = True

    return {'статус':'процесс запущен'}


@router.post('/stop-session')
async def stop_session(session: SessionDep = Depends(SessionDep)):
    global process_running
    if not process_running:
        raise HTTPException(status_code = 400, detail = 'Процесс не запущен')
    return {'статус': 'процесс остановлен'}


