from pydantic import BaseModel, EmailStr


class TokenModel(BaseModel):
    auth_token: str
    token_type: str


class LoginModel(BaseModel):
    email: EmailStr
    password: str
