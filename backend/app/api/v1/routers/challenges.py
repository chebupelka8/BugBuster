from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from models import ChallengeModel, ChallengeDifficulty
from schemas import CreateChallenge

from core.database import AbstractDataBase

import subprocess


router = APIRouter(
    prefix="/challenge",
    tags=["Challenges"]
)


@router.post("/new")
async def create_challenge(author_id: int, challenge: CreateChallenge):
    async def add_new(session: AsyncSession):
        new_challenge = ChallengeModel(
            author_id=author_id, **challenge.model_dump()
        )

        session.add(new_challenge)
    
    await AbstractDataBase.run_in_session_with_commit(add_new)



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

