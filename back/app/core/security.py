from datetime import datetime, timedelta, UTC
from hashlib import sha256
import jwt


def create_jwt(data: dict):
    data.update({'exp': datetime.now(UTC) + timedelta(hours=24)})
    return jwt.encode(data, 'secret', algorithm='HS256')


def read_jwt(token: str):
    return jwt.decode(token, 'secret', algorithm='HS256')


def hash_password(password: str):
    return sha256(password.encode('utf-8')).digest()