
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel

class Person(Base, BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    cpf = Column(String, unique=True, index=True, nullable=True)
    birth = Column(String, nullable=False) # Consider using Date type if appropriate

    user = relationship("User", back_populates="person", uselist=False)

