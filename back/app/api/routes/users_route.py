from fastapi import APIRouter, HTTPException, Depends, Body, status

from typing import Annotated
from sqlmodel import select

from back.app.models.users_models import User, UserGetWithGroup, UserPost, UserPatch
from back.app.api.deps import SessionDep, UserDep, AdminDep
from back.app.models.groups_models import Group
from back.app.core.security import hash_password

router = APIRouter(prefix = '/users')


@router.get('/', response_model=list[UserGetWithGroup])
async def get_users(session: SessionDep):
    users = session.exec(select(User)).all()

    if not users:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

    return users


@router.post('/', response_model=UserGetWithGroup, status_code=status.HTTP_201_CREATED)
async def create_user(data: Annotated[UserPost, Depends()], session: SessionDep, admin: AdminDep):
    user = User.model_validate(data, update={'password_hash': hash_password(data.password)})
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.patch('/', response_model=UserGetWithGroup)
async def update_user(data: Annotated[UserPatch, Depends()], session: SessionDep, user: UserDep):
    target = session.get(User, data.uuid)

    if not target:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    if target.uuid != user.uuid and (user.category != 2 or target.category == 2):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    data_dict = data.model_dump(exclude_none=True)

    if data.group_id:
        new_group = session.get(Group, data.group_id)
        if not new_group:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Group not found')
        data_dict.update({'group': new_group})

    target.sqlmodel_update(data_dict)
    session.add(target)
    session.commit()
    session.refresh(target)
    return target


@router.delete('/', response_model=UserGetWithGroup)
def delete_user(session: SessionDep, admin: AdminDep, uuid: str = Body(embed=True)):
    user = session.get(User, uuid)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    session.delete(user)
    session.commit()
    return {'detail': 'OK'}

