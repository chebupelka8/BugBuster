from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text

from fastapi import HTTPException

from models import SolutionModel, ChallengeModel
from schemas import Solution, CreateSolution, RunnableSolution

from core.database import DataBase


import subprocess


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
    
    @classmethod
    async def __delete_solution_by_id(cls, session: AsyncSession, id: int) -> Solution:
        solution = await cls.__get_solution_by_id(session, id)
        await session.delete(solution)

        return solution

        # if (target := await session.get(SolutionModel, id)) is not None:
        #     await session.delete(target)

        #     return Solution(**target.dump())
        # else:
        #     raise HTTPException(status_code=404, detail="Solution not found")
    
    @classmethod
    async def delete_solution_by_id(cls, id: int) -> Solution:
        return await cls.run_in_session_with_commit(
            cls.__delete_solution_by_id, id
        )
    
    @staticmethod
    async def __get_solution_by_id(session: AsyncSession, id: int) -> Solution:
        """returns detached object"""

        if (target := await session.get(SolutionModel, id)) is not None:
            return Solution(**target.dump())
        else:
            raise HTTPException(status_code=404, detail="Solution not found")
    
    @classmethod
    async def send_solution(cls, id: int):
        async with cls.session() as session:
            statement = (
                select(SolutionModel.code, SolutionModel.status, ChallengeModel.callable_name, ChallengeModel.test_cases).select_from(SolutionModel)
                    .join(ChallengeModel, SolutionModel.challenge_id == ChallengeModel.id)
                    .where(SolutionModel.id == id)
            )

            result = await session.execute(statement)

            if (returning := result.mappings().first()) is not None:
                print(returning)
                return RunnableSolution(**returning)
            else:
                raise HTTPException(status_code=404, detail="Solution not found")
            

