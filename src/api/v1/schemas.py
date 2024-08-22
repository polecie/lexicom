from typing import Annotated

from pydantic import BaseModel, Field


class Phone(BaseModel):
    phone: Annotated[str, Field(..., pattern=r"^8\d{10}$")]


class Address(BaseModel):
    address: str

    class Config:
        from_attributes = True


class RequestData(BaseModel):
    phone: Annotated[str, Field(..., pattern=r"^8\d{10}$")]
    address: str


class Name(BaseModel):
    name: str
    status: int

    class Config:
        from_attributes = True
