from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException

from models import SolutionModel
from schemas import Solution, CreateSolution

from core.database import DataBase


class SolutionsRepository(DataBase):

    @staticmethod
    async def __add_solution(session: AsyncSession, solution: SolutionModel) -> Solution:
        session.add(solution)

        await session.flush()

        return Solution(**solution.dump())
    
    @classmethod
    async def add_solution(cls, solution: CreateSolution) -> Solution:
        return await cls.run_in_session_with_commit(
            cls.__add_solution, SolutionModel(**solution.model_dump())
        )
    
    @staticmethod
    async def __delete_solution_by_id(session: AsyncSession, id: int) -> Solution:
        if (target := await session.get(SolutionModel, id)) is not None:
            await session.delete(target)

            return Solution(**target.dump())
        else:
            raise HTTPException(status_code=404, detail="Solution not found")
    
    @classmethod
    async def delete_solution_by_id(cls, id: int) -> Solution:
        return await cls.run_in_session_with_commit(
            cls.__delete_solution_by_id, id
        )
