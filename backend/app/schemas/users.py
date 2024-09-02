from pydantic import BaseModel, EmailStr

from typing import Optional
from datetime import datetime

from models import UserRole

from core.reused_types import PydanticTypes


class CreateUser(BaseModel):
    username: PydanticTypes.string64
    email: Optional[EmailStr] = None
    password: PydanticTypes.string128
    role: UserRole = UserRole.member


class User(CreateUser):
    id: int

    created_at: datetime
    updated_at: datetime


class SecureUser(BaseModel):
    id: int

    username: PydanticTypes.string64
    email: Optional[EmailStr] = None
    role: UserRole = UserRole.member

    created_at: datetime
    updated_at: datetime

