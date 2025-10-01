
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel
from app.models.enums import RoleEnum

class User(Base, BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"), unique=True, nullable=False)
    active = Column(Boolean, default=True)
    role = Column(Enum(RoleEnum), default=RoleEnum.USER, nullable=False)

    person = relationship("Person", back_populates="user")
    userConfig = relationship("UserConfig", back_populates="user", uselist=False)

