from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from back.app.models.groups_models import Group
from back.app.api.deps import SessionDep
from sqlmodel import select
from back.app.models.groups_models import Group, GroupPost

router = APIRouter(prefix = '/groups')

@router.get("/", response_model=list[Group])
async def get_groups(session: SessionDep):
    groups = session.exec(
        select(Group)
    ).all()
    if not groups:
        raise HTTPException(status_code=204)
    return groups

@router.post("/", response_model=Group)
async def create_group(data: Annotated[GroupPost, Depends()], session: SessionDep):
    group = Group.model_validate(data.model_dump())
    session.add(group)
    session.commit()

    return {'detail': 'OK'}

@router.delete("/")
async def delete_group(session: SessionDep):
    group = session.get(Group)

    if not group:
        raise HTTPException(status_code=404, detail = 'Group not found')

    session.delete(group)
    session.commit()

    return {'detail':'OK'}
