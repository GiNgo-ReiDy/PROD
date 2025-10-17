from fastapi import APIRouter

from back.app.api.deps import LoginDep
from back.app.core.security import hash_password, create_jwt
from back.app.models import Token


router = APIRouter(prefix='/auth')


@router.post('/login', response_model=Token)
def user_login(user: LoginDep):
    data = {
        'sub': user.login,
        'pwd': hash_password(user.password).hex(),
    }
    jwt = create_jwt(data)
    return Token(access_token=jwt)