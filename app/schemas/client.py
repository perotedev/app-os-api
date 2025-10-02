
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.base import MetaData
from app.schemas.address import AddressInClient

class ClientBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    cnpj: Optional[str] = None

class ClientCreate(ClientBase):
    address: AddressInClient

class ClientUpdate(ClientBase):
    name: Optional[str] = None
    address: Optional[AddressInClient] = None

class ClientInDBBase(ClientBase, MetaData):
    id: Optional[int] = None
    address_id: Optional[int] = None
    address: Optional[AddressInClient] = None

    class Config:
        from_attributes = True

class ClientResume(BaseModel):
    name: str

class Client(ClientInDBBase):
    pass

