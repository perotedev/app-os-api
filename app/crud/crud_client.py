from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate
from app.crud.crud_address import address as crud_address

class CRUDClient(CRUDBase[Client, ClientCreate, ClientUpdate]):
    def create(self, db: Session, *, obj_in: ClientCreate) -> Client:
        address_in = obj_in.address
        db_address = crud_address.create(db, obj_in=address_in)
        
        obj_in_data = obj_in.model_dump(exclude={"address"})
        db_obj = self.model(**obj_in_data, address_id=db_address.id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Client, obj_in: Union[ClientUpdate, Dict[str, Any]]
    ) -> Client:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        
        if "address" in update_data and update_data["address"] is not None:
            address_update_data = update_data.pop("address")
            crud_address.update(db, db_obj=db_obj.address, obj_in=address_update_data)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

client = CRUDClient(Client)

