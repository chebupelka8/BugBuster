from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException

from schemas import UpdateChallenge, CreateChallenge, Challenge
from models import ChallengeModel

from core.database import DataBase


class ChallengesRepository(DataBase):

    @staticmethod
    async def __add_challenge(session: AsyncSession, challenge: ChallengeModel) -> Challenge:
        session.add(challenge)
        
        await session.flush()

        return Challenge(**challenge.dump())
    
    @classmethod
    async def add_challenge(cls, challenge: CreateChallenge) -> Challenge:
        return await cls.run_in_session_with_commit(
            cls.__add_challenge, ChallengeModel(**challenge.model_dump())
        )
    
    @staticmethod
    async def __delete_challenge_by_id(session: AsyncSession, id: int) -> Challenge:
        if (target := await session.get(ChallengeModel, id)) is not None:
            await session.delete(target)

            return Challenge(**target.dump())
        else:
            raise HTTPException(status_code=404, detail="Challenge not found")
    
    @classmethod
    async def delete_challenge_by_id(cls, id: int) -> Challenge:
        return await cls.run_in_session_with_commit(
            cls.__delete_challenge_by_id, id
        )
