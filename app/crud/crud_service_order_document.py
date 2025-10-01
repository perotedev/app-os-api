
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.service_order_document import ServiceOrderDocument
from app.schemas.service_order import ServiceOrderDocumentCreate, ServiceOrderDocumentUpdate

class CRUDServiceOrderDocument(CRUDBase[ServiceOrderDocument, ServiceOrderDocumentCreate, ServiceOrderDocumentUpdate]):
    pass

service_order_document = CRUDServiceOrderDocument(ServiceOrderDocument)

