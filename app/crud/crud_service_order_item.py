from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.service_order_item import ServiceOrderItem
from app.schemas.service_order import ServiceOrderItemCreate, ServiceOrderItemUpdate

class CRUDServiceOrderItem(CRUDBase[ServiceOrderItem, ServiceOrderItemCreate, ServiceOrderItemUpdate]):
    pass

service_order_item = CRUDServiceOrderItem(ServiceOrderItem)

