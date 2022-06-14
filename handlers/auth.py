from fastapi import APIRouter, Depends, HTTPException, status, Request
from models.credentials import TokenModel, LoginModel
from depends.collector import get_user_collector
from depends.users import UsersCollector
from security.credentials import verify_password, create_access_token
from security.credentials import decode_access_token


router = APIRouter()


@router.post("/", response_model=TokenModel)
async def create_token(login: LoginModel, users: UsersCollector = Depends(get_user_collector)):
    user = await users.get_by_email(login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Не правильный пароль или email")

    validation_token = decode_access_token(user.auth_token) if user.auth_token else None
    token = user.auth_token if validation_token else create_access_token({"sub": user.email})

    if user.auth_token != token:
        await users.update_token(user.id, token)

    return TokenModel(
        auth_token=token,
        token_type="Bearer"
    )

