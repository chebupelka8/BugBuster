from pydantic import BaseModel
from datetime import datetime

from models import SolutionStatus


class UpdateSolution(BaseModel):
    code: str
    status: SolutionStatus = SolutionStatus.uncompleted


class CreateSolution(UpdateSolution):
    author_id: int
    challenge_id: int


class Solution(CreateSolution):
    id: int
    sent_at: datetime
