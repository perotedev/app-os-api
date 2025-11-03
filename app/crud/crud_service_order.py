
from typing import Any, Dict, Union
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.service_order import ServiceOrder
from app.models.service_order_item import ServiceOrderItem
from app.schemas.service_order import ServiceOrderCreate, ServiceOrderUpdate, ServiceOrderItemCreate, ServiceOrderDocumentCreate
from app.crud.crud_service_order_item import service_order_item as crud_service_order_item
from app.crud.crud_service_order_document import service_order_document as crud_service_order_document

class CRUDServiceOrder(CRUDBase[ServiceOrder, ServiceOrderCreate, ServiceOrderUpdate]):
    def create(self, db: Session, *, obj_in: ServiceOrderCreate) -> ServiceOrder:
        db_obj = ServiceOrder(**obj_in.dict(exclude_unset=True, exclude={"items", "documents"}))
        add_items = []

        if obj_in.items:
            for item_in in obj_in.items:
                add_items.append(ServiceOrderItem(**item_in.dict(exclude_unset=True)))
                
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: ServiceOrder, obj_in: Union[ServiceOrderUpdate, Dict[str, Any]]
    ) -> ServiceOrder:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

service_order = CRUDServiceOrder(ServiceOrder)

