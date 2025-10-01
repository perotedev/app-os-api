
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel

class UserConfig(Base, BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), unique=True, nullable=False)
    theme = Column(String, default="light")
    notifications_enabled = Column(Boolean, default=True)

    user = relationship("User", back_populates="userConfig")

