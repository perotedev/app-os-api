
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.service_type import ServiceType
from app.schemas.service_type import ServiceTypeCreate, ServiceTypeUpdate

class CRUDServiceType(CRUDBase[ServiceType, ServiceTypeCreate, ServiceTypeUpdate]):
    pass

service_type = CRUDServiceType(ServiceType)

