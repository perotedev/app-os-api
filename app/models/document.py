
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel

class Document(Base, BaseModel):
    __tablename__ = 'document'
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_type = Column(String, nullable=False)

    contract_documents = relationship("ContractDocument", back_populates="document")
    service_order_documents = relationship("ServiceOrderDocument", back_populates="document")
    service_order_item_documents = relationship("ServiceOrderItemDocument", back_populates="document")

