from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from .abstract_model import AbstractModel

from core.reused_types import SQLAlchemyTypes


class SolutionModel(AbstractModel):
    __tablename__ = "solutions"

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    challenge_id: Mapped[int] = mapped_column(ForeignKey("challenges.id"))
    code: Mapped[str]

    sent_at: Mapped[SQLAlchemyTypes.created_at_utc]
