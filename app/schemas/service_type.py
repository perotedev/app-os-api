
from typing import Optional

from pydantic import BaseModel

from app.schemas.base import MetaData

class ServiceTypeBase(BaseModel):
    name: str
    icon: str
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

class ServiceTypeResume(BaseModel):
    name: str
    icon: str


class ServiceType(ServiceTypeInDBBase):
    pass

