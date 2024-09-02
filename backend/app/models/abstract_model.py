from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, validates
from sqlalchemy import inspect

from prettytable import PrettyTable


class AbstractModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @validates("id")
    def validate_id(self, _, value: int):
        if value <= 0:
            raise ValueError(
                "ID must be greater than 0."
            )
        
        return value
    
    should_use_table_view: bool = True

    def __repr__(self) -> str:
        dumped = self.dump()

        insp = inspect(self)
        conditions = filter(lambda attr: getattr(insp, attr), ["transient", "pending", "persistent", "deleted", "detached"])

        if self.should_use_table_view:

            preview = PrettyTable([
                f"{self.__class__.__name__}({self.__tablename__})",
                *dumped.keys(),
                "condition"
            ])
            preview.add_row(["", *dumped.values(), "\n".join(conditions)])

            return preview.get_string()

        return f"{self.__class__.__name__}(__tablename__={self.__tablename__}, condition={list(conditions)}, {dumped})"
    
    @property
    def column_names(self) -> list[str]:
        return [column.name for column in self.__table__.columns]
    
    def dump(self) -> dict:
        return {
            key: self.__dict__[key] for key in self.__dict__ if isinstance(key, str) and not key.startswith("_")
        }

