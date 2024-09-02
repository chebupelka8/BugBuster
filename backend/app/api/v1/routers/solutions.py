from fastapi import APIRouter

from schemas import CreateSolution


router = APIRouter(
    prefix="/solutions",
    tags=["Solutions"]
)


@router.post("/send")
async def send_solution(solution: CreateSolution):
    ...
    