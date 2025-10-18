from typing import Annotated

from back.app.models.groups_models import Group, GroupPost, GroupGetWithUsers, GroupPatch
from back.app.models.shedules_models import SchedulePost, ScheduleGet

from fastapi import APIRouter, HTTPException, Depends, Body, status
from back.app.api.deps import SessionDep, AdminDep
from sqlmodel import select

router = APIRouter(prefix = '/groups')

@router.get("/", response_model=list[GroupGetWithUsers])
async def get_groups(session: SessionDep):
    groups = session.exec(
        select(Group)
    ).all()
    if not groups:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return groups

@router.post("/", response_model=Group, status_code=status.HTTP_201_CREATED)
async def create_group(data: Annotated[GroupPost, Depends()], session: SessionDep, admin: AdminDep):
    group = Group.model_validate(data.model_dump())
    session.add(group)
    session.commit()
    session.refresh(group)

    return group

@router.patch('/', response_model=Group)
def patch_group(data: Annotated[GroupPatch, Depends()], session: SessionDep, admin: AdminDep):
    group = session.get(Group, data.id)

    if not group:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Group not found")

    group.sqlmodel_update(data.model_dump(exclude_none=True))

    session.add(group)
    session.commit()
    session.refresh(group)

    return group

@router.delete("/")
async def delete_group(session: SessionDep, admin: AdminDep, id: int = Body(embed=True)):
    group = session.get(Group, id)

    if not group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = 'Group not found')

    session.delete(group)
    session.commit()

    return {'detail':'OK'}


@router.post('/schedule', response_model=ScheduleGet, status_code=status.HTTP_201_CREATED)
async def create_schedule(data: Annotated[SchedulePost, Depends()], session: SessionDep, admin: AdminDep):
    schedule = ScheduleGet.model_validate(data)
    session.add(schedule)
    session.commit()
    session.refresh(schedule)
    return schedule
