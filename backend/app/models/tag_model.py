from sqlalchemy.orm import Mapped

from .abstract_model import AbstractModel

from core.reused_types import SQLAlchemyTypes


class TagModel(AbstractModel):
    """stores only available tags for challenges"""

    __tablename__ = "tags"

    title: Mapped[SQLAlchemyTypes.string32]
