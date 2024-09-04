from pydantic import BaseModel
from datetime import datetime

from models import SolutionStatus

from core.reused_types import PydanticTypes


class UpdateSolution(BaseModel):
    code: str
    status: SolutionStatus = SolutionStatus.uncompleted


class CreateSolution(UpdateSolution):
    author_id: int
    challenge_id: int


class Solution(CreateSolution):
    id: int

    created_at: datetime
    updated_at: datetime


class RunnableSolution(UpdateSolution):
    callable_name: PydanticTypes.string64
    test_cases: str
