from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.core.config import settings
from app.models.enums import DocumentSOPositionEnum
from app.models.service_order_item import ServiceOrderItem, ServiceOrderItemDocument
from app.models.document import Document
from app.schemas.service_order import ServiceOrderItemCreate, ServiceOrderItemUpdate, UpdateServiceOrderItemStatus
from pathlib import Path
import uuid
import shutil
import os

class CRUDServiceOrderItem(CRUDBase[ServiceOrderItem, ServiceOrderItemCreate, ServiceOrderItemUpdate]):
    def update_status(
        self, 
        db: Session, 
        *,
        so_item_in: UpdateServiceOrderItemStatus,
    ) -> ServiceOrderItem:
        service_order_item = self.get(db, id=so_item_in.service_order_item_id)
        if not service_order_item:
            raise HTTPException(status_code=404, details="Service order item not found")

        service_order_item.status = so_item_in.status
        db.commit()
        db.refresh(service_order_item)
        return service_order_item
    
    def attach_document(
        self,
        db,
        *,
        service_order_item_id: int,
        file: UploadFile,
        position: DocumentSOPositionEnum,
    ) -> ServiceOrderItemDocument:
        if not file:
            raise HTTPException(status_code=400, detail="No file provided")
        
        project_dir = Path(__file__).resolve().parents[2]
        base_dir = project_dir / settings.UPLOAD_DIR
        base_upload_dir = base_dir / "so_items" / str(service_order_item_id)
        base_upload_dir.mkdir(parents=True, exist_ok=True)

        suffix = Path(file.filename).suffix or ""
        unique_name = f"{uuid.uuid4().hex}{suffix}"
        dest_path = base_upload_dir / unique_name

        with open(dest_path, "wb") as out_file:
            shutil.copyfileobj(file.file, out_file)
        file_path = str(dest_path.resolve())

        if not file_path:
            raise HTTPException(status_code=500, detail="Failed to save the uploaded file")

        new_document = Document(
            filename = file.filename,
            file_path = file_path,
            file_type = file.content_type,
            size = file.size
        )

        new_so_item_document = ServiceOrderItemDocument(
            service_order_item_id=service_order_item_id,
            position=position,
            document=new_document
        )

        db.add(new_so_item_document)
        db.commit()
        db.refresh(new_so_item_document)
        return new_so_item_document

service_order_item = CRUDServiceOrderItem(ServiceOrderItem)

