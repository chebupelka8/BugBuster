from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from .abstract_model import AbstractModel


class ChallengeTagModel(AbstractModel):
    __tablename__ = "challenge_tags"

    challenge_id: Mapped[int] = mapped_column(ForeignKey("challenges.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"))