
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.contract_document import ContractDocument
from app.schemas.contract import ContractDocumentCreate, ContractDocumentUpdate

class CRUDContractDocument(CRUDBase[ContractDocument, ContractDocumentCreate, ContractDocumentUpdate]):
    pass

contract_document = CRUDContractDocument(ContractDocument)

