from sqlalchemy.ext.asyncio import AsyncSession

from core.database import DataBase

from schemas import CreateUser, SecureUser, User
from models import UserModel


class UsersRepository(DataBase):

    @staticmethod
    async def __add_user(session: AsyncSession, user: UserModel) -> User:
        session.add(user)

        await session.flush()

        return User(**user.dump())

    @classmethod
    async def add_user(cls, user: CreateUser) -> User:
        return await cls.run_in_session_with_commit(
            cls.__add_user, UserModel(**user.model_dump())
        )
