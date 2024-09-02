from pydantic import BaseModel
from datetime import datetime

from models import SolutionStatus


class CreateSolution(BaseModel):
    author_id: int
    challenge_id: int

    code: str
    status: SolutionStatus = SolutionStatus.uncompleted


class Solution(CreateSolution):
    id: int
    sent_at: datetime
