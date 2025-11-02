
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.base import MetaData
from app.schemas.enums import RoleEnum
from app.schemas.person import Person, PersonCreate
from app.schemas.user_config import UserConfig

class UserBase(BaseModel):
    email: EmailStr
    active: Optional[bool] = True
    role: Optional[RoleEnum] = RoleEnum.USER
    person: PersonCreate

class UserCreate(UserBase):
    password: str
    person: Person

class UserUpdate(UserBase):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    person: Optional[Person] = None
    role: Optional[RoleEnum] = None

class UserCreateNoPass(UserUpdate):
    person: PersonCreate

class UserInDBBase(UserBase, MetaData):
    id: Optional[int] = None
    person_id: Optional[int] = None
    person: Optional[Person] = None
    user_config: Optional[UserConfig] = None

    class Config:
        from_attributes = True

class User(UserInDBBase):
    pass

class UserResume(UserBase):
    id: int
    person_id: int
    person: Person

    class Config:
        from_attributes = True

class UserInDB(UserInDBBase):
    hashed_password: str

