from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from back.app.core import engine
from back.app.core.security import read_jwt, hash_password
from back.app.models.users_models import User

from sqlmodel import Session, select
from typing import Annotated


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_session():
    with Session(engine) as session:
        yield session


def get_login(form: Annotated[OAuth2PasswordRequestForm, Depends()], session: "SessionDep"):
    # noinspection PyTypeChecker
    user = session.exec(
        select(User).where(User.login == form.username)
    ).one()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not hash_password(form.password) == user.password_hash:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    return user


def get_user(token: Annotated[str, Depends(oauth2_scheme)], session: "SessionDep"):
    data = read_jwt(token)
    uuid = data.get("sub")
    password_hash = data.get("pwd")

    user = session.get(User, uuid)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if user.password_hash.hex() != password_hash:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect password")

    return user


def get_admin_user(user: Annotated[User, Depends(get_user)]):
    if user.category == 2:
        return user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


SessionDep = Annotated[Session, Depends(get_session)]
LoginDep = Annotated[User, Depends(get_login)]
UserDep = Annotated[User, Depends(get_user)]
AdminDep = Annotated[User, Depends(get_admin_user)]

