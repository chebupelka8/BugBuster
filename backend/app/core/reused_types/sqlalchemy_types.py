from typing import Annotated

from datetime import datetime, UTC

from sqlalchemy import String
from sqlalchemy.orm import mapped_column


class SQLAlchemyTypes:

    string16 = Annotated[str, mapped_column(String(16))]
    string32 = Annotated[str, mapped_column(String(32))]
    string64 = Annotated[str, mapped_column(String(64))]
    string128 = Annotated[str, mapped_column(String(128))]
    string256 = Annotated[str, mapped_column(String(256))]

    created_at_utc = Annotated[
        datetime, mapped_column(default=lambda: datetime.now(UTC))
    ]

    updated_at_utc = Annotated[
        datetime, mapped_column(default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))
    ]
