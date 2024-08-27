from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, validates


class AbstractModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @validates("id")
    def validate_id(self, _, value: int):
        if value <= 0:
            raise ValueError(
                "ID must be greater than 0."
            )
        
        return value

