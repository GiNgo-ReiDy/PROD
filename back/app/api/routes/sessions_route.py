from fastapi import APIRouter, HTTPException
from back.app.api.deps import SessionDep
from datetime import datetime, timedelta
from back.app.models.sessions_models import Session
from back.app.api.deps import UserDep

router = APIRouter(prefix = '/sessions')


@router.post('/start')
async def start_process(user:UserDep, session: SessionDep):
    if user.session:
        raise HTTPException(status_code = 400, detail = 'You are already running this session')

    new_w = Session(
        start_time=datetime.now(),
        break_time=datetime.now() + timedelta(seconds=user.group.seconds_limitation),
    )
    user.session = new_w

    session.add(user)
    session.commit()


    return {'detail':'OK'}


@router.post('/stop')
async def stop_process(user:UserDep, session: SessionDep):
    if not user.session:
        raise HTTPException(status_code = 204, detail = 'There is no active session')

    new_w = Session(
        stop_time = datetime.now()
    )
    user.session = new_w
    session.add(user)
    session.commit()
    return {'detail': 'OK'}


