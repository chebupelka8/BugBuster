from pydantic import BaseModel

from datetime import datetime
from typing import Optional

from models import ChallengeDifficulty

from core.reused_types import PydanticTypes


class CreateChallenge(BaseModel):
    title: PydanticTypes.string32
    description: Optional[PydanticTypes.string128] = None
    long_description: str
    difficulty: ChallengeDifficulty = ChallengeDifficulty.easy

    initial_code: str = ""
    solution: str


class Challenge(CreateChallenge):
    id: int
    author_id: int

    created_at: datetime
    updated_at: datetime