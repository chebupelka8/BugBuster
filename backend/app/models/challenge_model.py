from typing import Optional
from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from .abstract_model import AbstractModel

from core.reused_types import SQLAlchemyTypes


class ChallengeDifficulty(str, Enum):
    easy = "Easy"
    medium = "Medium"
    hard = "Hard"
    extreme = "Extreme"


class ChallengeModel(AbstractModel):
    __tablename__ = "challenges"

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[SQLAlchemyTypes.string32]
    description: Mapped[Optional[SQLAlchemyTypes.string128]]
    long_description: Mapped[str]
    difficulty: Mapped[ChallengeDifficulty]

    callable_name: Mapped[SQLAlchemyTypes.string64]
    test_cases: Mapped[str]

    initial_code: Mapped[str] = mapped_column(default="")
    solution: Mapped[str]
    
    created_at: Mapped[SQLAlchemyTypes.created_at_utc]
    updated_at: Mapped[SQLAlchemyTypes.updated_at_utc]
