
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel
from app.models.enums import ServiceOrderStatusEnum

class ServiceOrder(Base, BaseModel):
    __tablename__ = 'service_order'
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    contract_id = Column(Integer, ForeignKey("contract.id"), nullable=True)
    description = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    status = Column(Enum(ServiceOrderStatusEnum), default=ServiceOrderStatusEnum.PENDING, nullable=False)
    location = Column(String, nullable=True, default="")

    client = relationship("Client", back_populates="service_orders")
    contract = relationship("Contract", back_populates="service_orders")
    items = relationship("ServiceOrderItem", back_populates="service_order")
    documents = relationship("ServiceOrderDocument", back_populates="service_order")

