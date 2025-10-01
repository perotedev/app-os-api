
from typing import Optional, List

from pydantic import BaseModel, EmailStr

from app.schemas.base import MetaData
from app.schemas.address import Address

class ClientBase(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    cnpj: Optional[str] = None

class ClientCreate(ClientBase):
    address: Address

class ClientUpdate(ClientBase):
    name: Optional[str] = None
    address: Optional[Address] = None

class ClientInDBBase(ClientBase, MetaData):
    id: Optional[int] = None
    address_id: Optional[int] = None
    address: Optional[Address] = None

    class Config:
        from_attributes = True

class Client(ClientInDBBase):
    pass

