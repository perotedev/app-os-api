
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user_config import UserConfig
from app.schemas.user_config import UserConfigCreate, UserConfigUpdate

class CRUDUserConfig(CRUDBase[UserConfig, UserConfigCreate, UserConfigUpdate]):
    pass

user_config = CRUDUserConfig(UserConfig)

