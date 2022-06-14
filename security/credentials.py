import datetime
from fastapi.security import HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param
from fastapi import Request, HTTPException, status
from config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from passlib.context import CryptContext
from jose import jwt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashed_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hash: str) -> bool:
    return pwd_context.verify(password, hash)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    try:
        encoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except jwt.JWTError:
        return None
    else:
        return encoded_jwt


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):

        authorization: str = request.headers.get("Authorization")
        exp = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Не авторизирован")

        if authorization:
            scheme, credentials = get_authorization_scheme_param(authorization)
            if credentials:
                token = decode_access_token(credentials)
                if token is None:
                    raise exp

            if scheme.lower() != "bearer":
                if self.auto_error:
                    raise exp
                else:
                    return None

            return credentials

        return None



