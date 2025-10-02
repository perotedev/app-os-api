
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel

class ServiceOrderItem(Base, BaseModel):
    __tablename__ = 'service_order_item'
    id = Column(Integer, primary_key=True, index=True)
    service_order_id = Column(Integer, ForeignKey("service_order.id"), nullable=False)
    description = Column(String, nullable=False)
    notes = Column(String, nullable=True)

    service_order = relationship("ServiceOrder", back_populates="items")
    documents = relationship("ServiceOrderItemDocument", back_populates="service_order_item")

class ServiceOrderItemDocument(Base, BaseModel):
    __tablename__ = 'service_order_item_document'
    id = Column(Integer, primary_key=True, index=True)
    service_order_item_id =  Column(Integer, ForeignKey("service_order_item.id"), nullable=False)
    document_id = Column(Integer, ForeignKey("document.id"), nullable=False)
    document = relationship("Document")
    service_order_item = relationship("ServiceOrderItem", back_populates="documents")