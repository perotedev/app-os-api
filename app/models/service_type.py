
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel

class ServiceType(Base, BaseModel):
    __tablename__ = 'service_type'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    icon = Column(String, nullable=False)

    service_orders = relationship("ServiceOrder", back_populates="service_type")

