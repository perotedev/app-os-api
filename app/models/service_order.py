
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

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
    location = Column(String, nullable=True, default="")

    client = relationship("Client", back_populates="service_orders")
    contract = relationship("Contract", back_populates="service_orders")
    items = relationship("ServiceOrderItem", back_populates="service_order")
    documents = relationship("ServiceOrderDocument", back_populates="service_order")

    @hybrid_property
    def status(self) -> str:
        statuses = []
        for item in self.items:
            if item.status is None:
                continue
            statuses.append(item.status)

        if not statuses:
            return ServiceOrderStatusEnum.PENDING

        if all(s == "PENDING" for s in statuses):
            return ServiceOrderStatusEnum.PENDING

        if any(s == "IN_PROGRESS" for s in statuses):
            return ServiceOrderStatusEnum.IN_PROGRESS

        if all(s in ("FINISHED", "CANCELED") for s in statuses):
            return ServiceOrderStatusEnum.FINISHED

        return ServiceOrderStatusEnum.IN_PROGRESS

