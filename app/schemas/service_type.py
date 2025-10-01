
from typing import Optional

from pydantic import BaseModel

from app.schemas.base import MetaData

class ServiceTypeBase(BaseModel):
    name: str
    description: Optional[str] = None

class ServiceTypeCreate(ServiceTypeBase):
    pass

class ServiceTypeUpdate(ServiceTypeBase):
    name: Optional[str] = None
    description: Optional[str] = None

class ServiceTypeInDBBase(ServiceTypeBase, MetaData):
    id: Optional[int] = None

    class Config:
        from_attributes = True

class ServiceType(ServiceTypeInDBBase):
    pass

