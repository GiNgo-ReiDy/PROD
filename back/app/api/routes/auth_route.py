from fastapi import APIRouter
from pydantic import BaseModel
from back.app.core.security import hash_password, create_jwt
from back.app.models import Token

router = APIRouter(prefix='/auth')

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post('/login', response_model=Token)
def user_login(user: LoginRequest):
    # Пример логики
    hashed_pwd = hash_password(user.password)
    data = {
        'sub': user.username,
        'pwd': hashed_pwd.hex(),
    }
    jwt = create_jwt(data)
    return Token(access_token=jwt)
