
from typing import Optional

from pydantic import BaseModel

from app.schemas.base import MetaData

class AddressBase(BaseModel):
    street: str
    number: str
    complement: Optional[str] = None
    neighborhood: str
    city: str
    state: str
    cep: str

class AddressCreate(AddressBase):
    pass

class AddressUpdate(AddressBase):
    street: Optional[str] = None
    number: Optional[str] = None
    neighborhood: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    cep: Optional[str] = None

class AddressInDBBase(AddressBase, MetaData):
    id: Optional[int] = None

    class Config:
        from_attributes = True

class AddressInClient(BaseModel):
    id: Optional[int] = None
    street: Optional[str] = None
    number: Optional[str] = None
    neighborhood: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    cep: Optional[str] = None

    class Config:
        from_attributes = True

class Address(AddressInDBBase):
    pass

