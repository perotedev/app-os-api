
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.base import MetaData
from app.schemas.enums import RoleEnum
from app.schemas.person import Person
from app.schemas.user_config import UserConfig

class UserBase(BaseModel):
    email: EmailStr
    active: Optional[bool] = True
    role: Optional[RoleEnum] = RoleEnum.USER

class UserCreate(UserBase):
    password: str
    person: Person

class UserUpdate(UserBase):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    person: Optional[Person] = None
    role: Optional[RoleEnum] = None

class UserInDBBase(UserBase, MetaData):
    id: Optional[int] = None
    person_id: Optional[int] = None
    person: Optional[Person] = None
    userConfig: Optional[UserConfig] = None

    class Config:
        from_attributes = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    hashed_password: str

