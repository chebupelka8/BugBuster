from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete

from core.database import DataBase

from schemas import CreateUser, User
from models import UserModel


class UsersRepository(DataBase):

    @staticmethod
    async def __add_user(session: AsyncSession, user: UserModel) -> User:
        session.add(user)

        await session.flush()

        return User(**user.dump())
    
    @staticmethod
    async def __get_user(session: AsyncSession, id: int):
        ...

    @classmethod
    async def add_user(cls, user: CreateUser) -> User:
        return await cls.run_in_session_with_commit(
            cls.__add_user, UserModel(**user.model_dump())
        )

    @staticmethod
    async def __delete_user_by_id(session: AsyncSession, id: int) -> User:
        if (target := await session.get(UserModel, id)) is not None:
            await session.delete(target)

            return User(**target.dump())
        else:
            raise HTTPException(404, detail="User not found")
    
    @classmethod
    async def delete_user(cls, id: int) -> User:
        return await cls.run_in_session_with_commit(
            cls.__delete_user_by_id, id
        )
