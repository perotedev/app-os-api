
from typing import Optional
from datetime import date

from pydantic import BaseModel

from app.schemas.base import MetaData

class PersonBase(BaseModel):
    name: str
    phone: Optional[str] = None
    cpf: Optional[str] = None
    birth: date # Assuming birth is a date string in ISO format

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    name: Optional[str] = None
    birth: Optional[date] = None

class PersonInDBBase(PersonBase, MetaData):
    id: Optional[int] = None

    class Config:
        from_attributes = True

class Person(PersonInDBBase):
    pass

