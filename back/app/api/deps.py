from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from back.app.core import engine
from back.app.core.security import read_jwt
from back.app.models.users_models import User

from sqlmodel import Session, select
from typing import Annotated

def get_session():
    with Session(engine) as session:
        yield session


def get_login(form: OAuth2PasswordRequestForm, session: "SessionDep"):
    # noinspection PyTypeChecker
    user = session.exec(
        select(User).where(User.login == form.username)
    ).one()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user


def get_user(token: "TokenDep", session: "SessionDep"):
    data = read_jwt(token)
    uuid = data.get("uuid")

    user = session.get(User, uuid)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user


def get_admin_user(user: Annotated[User, Depends(get_user)]):
    if user.category == 2:
        return user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")
TokenDep = Annotated[str, Depends(oauth2_scheme)]

SessionDep = Annotated[Session, Depends(get_session)]
LoginDep = Annotated[User, Depends(get_login)]
UserDep = Annotated[User, Depends(get_user)]
AdminDep = Annotated[User, Depends(get_admin_user)]

