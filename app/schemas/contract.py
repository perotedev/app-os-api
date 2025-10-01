
from typing import Optional, List
from datetime import date

from pydantic import BaseModel

from app.schemas.base import MetaData
from app.schemas.document import Document

class ContractDocumentBase(BaseModel):
    document_id: int

class ContractDocumentCreate(ContractDocumentBase):
    pass

class ContractDocumentUpdate(ContractDocumentBase):
    document_id: Optional[int] = None

class ContractDocumentInDBBase(ContractDocumentBase, MetaData):
    id: Optional[int] = None
    contract_id: Optional[int] = None
    document: Optional[Document] = None

    class Config:
        from_attributes = True

class ContractDocument(ContractDocumentInDBBase):
    pass

class ContractBase(BaseModel):
    client_id: int
    number: str
    date_start: date
    date_end: date
    value: float

class ContractCreate(ContractBase):
    document_list: Optional[List[ContractDocumentCreate]] = None

class ContractUpdate(ContractBase):
    client_id: Optional[int] = None
    number: Optional[str] = None
    date_start: Optional[date] = None
    date_end: Optional[date] = None
    value: Optional[float] = None
    document_list: Optional[List[ContractDocumentUpdate]] = None

class ContractInDBBase(ContractBase, MetaData):
    id: Optional[int] = None
    documents: Optional[List[ContractDocument]] = None

    class Config:
        from_attributes = True

class Contract(ContractInDBBase):
    pass

