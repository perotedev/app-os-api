
from typing import Optional

from pydantic import BaseModel
from app.schemas.person import PersonBase
from app.schemas.user_config import UserConfig
from app.schemas.enums import RoleEnum

class UserResume(BaseModel):
    id: int
    email: str
    person: PersonBase
    active: bool
    role: RoleEnum
    userConfig: UserConfig

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResume

class TokenPayload(BaseModel):
    sub: Optional[int] = None

