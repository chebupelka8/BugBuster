from typing import Annotated

from pydantic import Field


class PydanticTypes:

    type string16 = Annotated[str, Field(max_length=16)]
    type string32 = Annotated[str, Field(max_length=32)]
    type string64 = Annotated[str, Field(max_length=64)]
    type string256 = Annotated[str, Field(max_length=256)]
