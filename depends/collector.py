from typing import Optional
from fastapi import status, HTTPException
from db.base import database
from depends.users import UsersCollector
from models.users import UserModel
from fastapi import Depends
from security.credentials import JWTBearer, decode_access_token


async def get_user_collector() -> UsersCollector:
    return UsersCollector(database)


async def get_current_user(
        users: UsersCollector = Depends(get_user_collector),
        token: Optional[str] = Depends(JWTBearer())
) -> Optional[UserModel]:

    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Учетные данные недействительны")

    if token:
        payload_token = decode_access_token(token)

        if payload_token is None:
            raise cred_exception

        email: str = payload_token.get("sub")
        if email is None:
            raise cred_exception

        user = await users.get_by_email(email=email)
        if user is None:
            raise cred_exception

        return user
    return None


