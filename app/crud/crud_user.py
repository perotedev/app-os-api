
from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.models.person import Person
from app.models.user_config import UserConfig
from app.schemas.user import UserCreate, UserUpdate, UserCreateNoPass
from app.core.security import get_password_hash

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def _get_default_user_config(self) -> UserConfig:
        return UserConfig(
            theme ="light",
            notifications_enabled = True
        )

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            person=Person(**obj_in.person.dict(exclude_unset=True)),
            active=obj_in.active,
            role=obj_in.role,
            user_config=self._get_default_user_config()
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def create_user_without_pass(self, db:Session, *, obj_in: UserCreateNoPass) -> User:
        db_obj = User(
            email=obj_in.email,
            person=Person(**obj_in.person.dict(exclude_unset=True)),
            active=obj_in.active,
            role=obj_in.role,
            user_config=self._get_default_user_config()
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(self.model).filter(User.email == email).first()

user = CRUDUser(User)

