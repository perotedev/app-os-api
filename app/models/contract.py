
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel

class Contract(Base, BaseModel):
    __tablename__ = 'contract'
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    number = Column(String, unique=True, index=True, nullable=False)
    date_start = Column(Date, nullable=False)
    date_end = Column(Date, nullable=False)
    value = Column(Float, nullable=False)

    client = relationship("Client", back_populates="contracts")
    documents = relationship("ContractDocument", back_populates="contract")
    service_orders = relationship("ServiceOrder", back_populates="contract")

