from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from enum import Enum

from .abstract_model import AbstractModel

from core.reused_types import SQLAlchemyTypes


class SolutionStatus(str, Enum):
    completed = "Completed"
    uncompleted = "Uncompleted"


class SolutionModel(AbstractModel):
    __tablename__ = "solutions"

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    challenge_id: Mapped[int] = mapped_column(ForeignKey("challenges.id"))
    code: Mapped[str]
    status: Mapped[SolutionStatus] = mapped_column(default=SolutionStatus.uncompleted)

    sent_at: Mapped[SQLAlchemyTypes.created_at_utc]
