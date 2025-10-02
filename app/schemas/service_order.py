from typing import Optional, List
from datetime import date
from pydantic import BaseModel
from app.schemas.base import MetaData
from app.schemas.enums import ServiceOrderStatusEnum
from app.schemas.document import Document
from app.schemas.client import ClientResume
from app.schemas.service_type import ServiceTypeResume

class ServiceOrderItemBase(BaseModel):
    service_order_id: int
    service_type_id: int
    description: str
    notes: Optional[str]
    status: Optional[ServiceOrderStatusEnum] = ServiceOrderStatusEnum.PENDING

class ServiceOrderItemCreate(ServiceOrderItemBase):
    pass

class ServiceOrderItemUpdate(ServiceOrderItemBase):
    description: Optional[str] = None
    service_order_id: Optional[int]
    service_type_id: Optional[int]

class ServiceOrderItemInDBBase(ServiceOrderItemBase, MetaData):
    id: int
    service_order_id: Optional[int] = None
    service_type: ServiceTypeResume

    class Config:
        from_attributes = True

class ServiceOrderItem(ServiceOrderItemInDBBase):
    pass

class ServiceOrderDocumentBase(BaseModel):
    document_id: int

class ServiceOrderDocumentCreate(ServiceOrderDocumentBase):
    pass

class ServiceOrderDocumentUpdate(ServiceOrderDocumentBase):
    document_id: Optional[int] = None

class ServiceOrderDocumentInDBBase(ServiceOrderDocumentBase, MetaData):
    id: Optional[int] = None
    service_order_id: Optional[int] = None
    document: Optional[Document] = None

    class Config:
        from_attributes = True

class ServiceOrderDocument(ServiceOrderDocumentInDBBase):
    pass

class ServiceOrderBase(BaseModel):
    client_id: int
    contract_id: Optional[int] = None
    description: str
    start_date: date
    end_date: Optional[date] = None
    status: Optional[ServiceOrderStatusEnum] = ServiceOrderStatusEnum.PENDING
    location: Optional[str]

class ServiceOrderCreate(ServiceOrderBase):
    items: Optional[List[ServiceOrderItemCreate]] = None
    documents: Optional[List[ServiceOrderDocumentCreate]] = None

class ServiceOrderUpdate(ServiceOrderBase):
    client_id: Optional[int] = None
    contract_id: Optional[int] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[ServiceOrderStatusEnum] = None
    items: Optional[List[ServiceOrderItemUpdate]] = None
    documents: Optional[List[ServiceOrderDocumentUpdate]] = None

class ServiceOrderInDBBase(ServiceOrderBase, MetaData):
    id: Optional[int] = None
    items: Optional[List[ServiceOrderItem]] = None
    documents: Optional[List[ServiceOrderDocument]] = None
    client: ClientResume

    class Config:
        from_attributes = True

class ServiceOrderResume(ServiceOrderBase, MetaData):
    id: int
    client: ClientResume

class ServiceOrder(ServiceOrderInDBBase):
    pass
