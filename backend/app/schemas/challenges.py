from pydantic import BaseModel

from datetime import datetime
from typing import Optional

from models import ChallengeDifficulty

from core.reused_types import PydanticTypes


class UpdateChallenge(BaseModel):
    title: PydanticTypes.string32
    description: Optional[PydanticTypes.string128] = None
    long_description: str
    difficulty: ChallengeDifficulty = ChallengeDifficulty.easy

    callable_name: PydanticTypes.string64
    test_cases: str

    initial_code: str = ""
    solution: str


class CreateChallenge(UpdateChallenge):
    author_id: int


class Challenge(CreateChallenge):
    id: int

    created_at: datetime
    updated_at: datetime
