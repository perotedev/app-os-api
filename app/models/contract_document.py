
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base_model import Base as BaseModel

class ContractDocument(Base, BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey("contract.id"), nullable=False)
    document_id = Column(Integer, ForeignKey("document.id"), nullable=False)

    contract = relationship("Contract", back_populates="documents")
    document = relationship("Document", back_populates="contract_documents")

