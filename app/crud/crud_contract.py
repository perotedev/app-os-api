
from typing import Any, Dict, Optional, Union, List
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.crud.base import CRUDBase
from app.models.contract import Contract
from app.schemas.contract import ContractCreate, ContractUpdate, ContractDocumentCreate
from app.crud.crud_contract_document import contract_document as crud_contract_document

class CRUDContract(CRUDBase[Contract, ContractCreate, ContractUpdate]):
    def create(self, db: Session, *, obj_in: ContractCreate) -> Contract:
        obj_in_data = obj_in.model_dump(exclude={"document_list"})
        db_obj = self.model(**obj_in_data)

        current_year = f"{datetime.now(timezone.utc).year}"
        last_number = (
            db.query(func.max(self.model.number))
            .filter(self.model.number.like(f"%/{current_year}"))
            .scalar()
        )
        last_number = 0 if last_number is None else int(last_number.split("/")[0])
        next_number = last_number + 1
        contract_code = f"{next_number:03}/{current_year}"
        db_obj.number = contract_code
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        if obj_in.document_list:
            for doc_in in obj_in.document_list:
                crud_contract_document.create(db, obj_in=ContractDocumentCreate(contract_id=db_obj.id, document_id=doc_in.document_id))
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Contract, obj_in: Union[ContractUpdate, Dict[str, Any]]
    ) -> Contract:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        
        # Handle nested document_list update if needed
        # For simplicity, this example doesn't handle complex nested updates for lists
        # A more robust solution would involve comparing existing documents and adding/removing as necessary

        return super().update(db, db_obj=db_obj, obj_in=update_data)

contract = CRUDContract(Contract)

