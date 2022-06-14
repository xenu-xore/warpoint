from fastapi import APIRouter, Depends
from models.users import UserModel, UserInModel
from depends.collector import get_user_collector
from depends.users import UsersCollector

router = APIRouter()


@router.post("/", response_model=UserModel)
async def create_user(
        user: UserInModel,
        users: UsersCollector = Depends(get_user_collector), ):
    return await users.create(u=user)
