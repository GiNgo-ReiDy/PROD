from datetime import datetime, timedelta, UTC
from hashlib import sha256
import jwt


def hash_password(password):
    return sha256(password.encode()).digest()


def create_jwt(data: dict):
    data.update({'exp': datetime.now(UTC) + timedelta(hours=24)})
    return jwt.encode(data)