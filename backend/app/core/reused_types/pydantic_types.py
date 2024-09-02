from typing import Annotated

from pydantic import Field


class PydanticTypes:

    string16 = Annotated[str, Field(max_length=16)]
    string32 = Annotated[str, Field(max_length=32)]
    string64 = Annotated[str, Field(max_length=64)]
    string128 = Annotated[str, Field(max_length=128)]
    string256 = Annotated[str, Field(max_length=256)]
