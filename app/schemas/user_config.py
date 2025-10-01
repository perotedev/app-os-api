
from typing import Optional

from pydantic import BaseModel

from app.schemas.base import MetaData

class UserConfigBase(BaseModel):
    theme: Optional[str] = "light"
    notifications_enabled: Optional[bool] = True

class UserConfigCreate(UserConfigBase):
    pass

class UserConfigUpdate(UserConfigBase):
    pass

class UserConfigInDBBase(UserConfigBase, MetaData):
    id: Optional[int] = None
    user_id: Optional[int] = None

    class Config:
        from_attributes = True

class UserConfig(UserConfigInDBBase):
    pass

