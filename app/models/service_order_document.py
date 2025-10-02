
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel

class ServiceOrderDocument(Base, BaseModel):
    __tablename__ = 'service_order_document'
    id = Column(Integer, primary_key=True, index=True)
    service_order_id = Column(Integer, ForeignKey("service_order.id"), nullable=False)
    document_id = Column(Integer, ForeignKey("document.id"), nullable=False)

    service_order = relationship("ServiceOrder", back_populates="documents")
    document = relationship("Document", back_populates="service_order_documents")

