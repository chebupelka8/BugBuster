from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from models import ChallengeModel, ChallengeDifficulty
from schemas import UpdateChallenge, CreateChallenge, Challenge

from repositories import ChallengesRepository

from core.database import AbstractDataBase

import subprocess


router = APIRouter(
    prefix="/challenges",
    tags=["Challenges"]
)


@router.post("/add")
async def add_challenge(challenge: CreateChallenge) -> Challenge:
    return await ChallengesRepository.add_challenge(challenge)


@router.delete("/delete")
async def delete_challenge(id: int) -> Challenge:
    return await ChallengesRepository.delete_challenge_by_id(id)



@router.post("/{challenge_id}/run")
async def run_challenge(challenge_id: int):
    async def inner(session: AsyncSession):
        return await session.get(ChallengeModel, challenge_id)
    
    target = await AbstractDataBase.run_in_session(inner)

    if target is not None:
        result = subprocess.run(["python", "-c", target.initial_code], capture_output=True, text=True)

        return {
            "output": result.stdout,
            "error": result.stderr,
            "status_code": result.returncode
        }

