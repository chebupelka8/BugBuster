from typing import Any

from fastapi import APIRouter

from schemas import CreateUpdateUser, SecureUser
from repositories import UsersRepository


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/add", response_model=SecureUser)
async def add_user(user: CreateUpdateUser) -> Any: 
    return await UsersRepository.add_user(user)


@router.delete("/delete", response_model=SecureUser)
async def delete_user(id: int) -> Any:
    return await UsersRepository.delete_user_by_id(id)


@router.put("/update", response_model=SecureUser)
async def update_user(target_id: int, updated_data: CreateUpdateUser) -> Any:
    return await UsersRepository.update_user(target_id, updated_data)


@router.get("/get", response_model=SecureUser)
async def get_user(id: int) -> Any:
    return await UsersRepository.get_user_by_id(id)
