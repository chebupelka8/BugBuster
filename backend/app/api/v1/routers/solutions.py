from fastapi import APIRouter

from repositories import SolutionsRepository

from schemas import CreateSolution, Solution


router = APIRouter(
    prefix="/solutions",
    tags=["Solutions"]
)


@router.post("/add")
async def add_solution(solution: CreateSolution) -> Solution:
    return await SolutionsRepository.add_solution(solution)


@router.delete("/delete")
async def delete_solution(id: int) -> Solution:
    return await SolutionsRepository.delete_solution_by_id(id)


@router.post("/send")
async def send_solution(solution: CreateSolution):
    ...
    