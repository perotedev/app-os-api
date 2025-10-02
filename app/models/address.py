
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel

class Address(Base, BaseModel):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, nullable=False, default="")
    number = Column(String, nullable=False, default="")
    complement = Column(String, nullable=True)
    neighborhood = Column(String, nullable=False, default="")
    city = Column(String, nullable=False, default="")
    state = Column(String, nullable=False, default="")
    cep = Column(String, nullable=False, default="")

    clients = relationship("Client", back_populates="address")

