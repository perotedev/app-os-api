
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel

class Client(Base, BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)
    phone = Column(String, nullable=True)
    cnpj = Column(String, unique=True, index=True, nullable=True)
    address_id = Column(Integer, ForeignKey("address.id"), nullable=False)

    address = relationship("Address", back_populates="clients")
    contracts = relationship("Contract", back_populates="client")

