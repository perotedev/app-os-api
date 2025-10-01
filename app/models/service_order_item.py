
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel

class ServiceOrderItem(Base, BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    service_order_id = Column(Integer, ForeignKey("serviceorder.id"), nullable=False)
    description = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_value = Column(Float, nullable=False)
    total_value = Column(Float, nullable=False)

    service_order = relationship("ServiceOrder", back_populates="items")
    documents = relationship("ServiceOrderItemDocument", back_populates="service_order_item")

