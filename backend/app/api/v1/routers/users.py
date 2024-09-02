from typing import Optional, Any
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter

from models import UserModel, UserRole
from schemas import CreateUser, SecureUser
from repositories import UsersRepository

from core.database import AbstractDataBase


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/add", response_model=SecureUser)
async def add_user(user: CreateUser) -> Any: 
    return await UsersRepository.add_user(user)
