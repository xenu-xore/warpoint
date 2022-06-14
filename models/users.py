from typing import Optional
from pydantic import BaseModel, EmailStr, constr, validator


class UserModel(BaseModel):
    id: Optional[int]
    email: str
    hashed_password: str
    auth_token: str = None


class UserInModel(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    password2: str

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("Пароли не совпадают")
        return v


class UpdateToken(BaseModel):
    auth_token: str
