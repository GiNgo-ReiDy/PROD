from fastapi import APIRouter

from back.app.models import Token
from back.app.api.deps import LoginDep
from back.app.core.security import hash_password, create_jwt


router = APIRouter(prefix='/auth')


@router.post('/login')
def login(user: LoginDep):
    data = {
        'sub': user.login,
        'pwd': hash_password(user.password).hex(),
    }
    jwt = create_jwt(data)
    return data