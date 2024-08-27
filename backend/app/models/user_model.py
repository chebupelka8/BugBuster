from sqlalchemy.orm import Mapped, mapped_column

from .abstract_model import AbstractModel

from core.reused_types import SQLAlchemyTypes

from enum import Enum
from typing import Optional


class UserRole(str, Enum):
    member = "Member"
    moderator = "Moderator"
    admin = "Admin"


class UserModel(AbstractModel):
    __tablename__ = "users"

    username: Mapped[SQLAlchemyTypes.string64]
    email: Mapped[Optional[SQLAlchemyTypes.string128]]
    password: Mapped[SQLAlchemyTypes.string128]
    role: Mapped[UserRole] = mapped_column(default=UserRole.member)

    created_at: Mapped[SQLAlchemyTypes.created_at_utc]
    updated_at: Mapped[SQLAlchemyTypes.updated_at_utc]
