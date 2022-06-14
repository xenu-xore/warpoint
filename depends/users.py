from typing import Optional
from depends.base import BaseCollector
from db.users import Users
from models.users import UserModel, UserInModel, UpdateToken
from security.credentials import hashed_password


class UsersCollector(BaseCollector):
    async def get_by_email(self, email: str) -> Optional[UserModel]:
        query = Users.select().where(Users.columns.email == email)
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return UserModel.parse_obj(user)

    async def create(self, u: UserInModel) -> UserModel:
        user = UserModel(
            email=u.email,
            hashed_password=hashed_password(u.password)
        )
        values = {**user.dict()}
        values.pop("id", None)
        query = Users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update_token(self, _id: int, token: str):
        token = UpdateToken(
            auth_token=token
        )
        values = {**token.dict()}

        query = Users.update().where(Users.columns.id == _id).values(**values)
        await self.database.execute(query)