from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter

from models import UserModel, UserRole
from schemas import CreateUser

from core.database import AbstractDataBase


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/add")
async def add_user(user: CreateUser): 
    async def add(session: AsyncSession):
        new_user = UserModel(**user.model_dump())

        session.add(new_user)
    
    await AbstractDataBase.run_in_session_with_commit(add)
