
from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.service_order import ServiceOrder
from app.schemas.service_order import ServiceOrderCreate, ServiceOrderUpdate, ServiceOrderItemCreate, ServiceOrderDocumentCreate
from app.crud.crud_service_order_item import service_order_item as crud_service_order_item
from app.crud.crud_service_order_document import service_order_document as crud_service_order_document

class CRUDServiceOrder(CRUDBase[ServiceOrder, ServiceOrderCreate, ServiceOrderUpdate]):
    def create(self, db: Session, *, obj_in: ServiceOrderCreate) -> ServiceOrder:
        obj_in_data = obj_in.model_dump(exclude={"items", "documents"})
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        if obj_in.items:
            for item_in in obj_in.items:
                crud_service_order_item.create(db, obj_in=ServiceOrderItemCreate(service_order_id=db_obj.id, **item_in.model_dump()))
        
        if obj_in.documents:
            for doc_in in obj_in.documents:
                crud_service_order_document.create(db, obj_in=ServiceOrderDocumentCreate(service_order_id=db_obj.id, document_id=doc_in.document_id))
        
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: ServiceOrder, obj_in: Union[ServiceOrderUpdate, Dict[str, Any]]
    ) -> ServiceOrder:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        
        # Handle nested items and documents update if needed
        # For simplicity, this example doesn't handle complex nested updates for lists

        return super().update(db, db_obj=db_obj, obj_in=update_data)

service_order = CRUDServiceOrder(ServiceOrder)

