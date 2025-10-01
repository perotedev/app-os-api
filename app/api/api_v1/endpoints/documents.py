
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Document])
def read_documents(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve documents.
    """
    documents = crud.document.get_multi(db, skip=skip, limit=limit)
    return documents

@router.post("/", response_model=schemas.Document)
def create_document(
    *,
    db: Session = Depends(deps.get_db),
    document_in: schemas.DocumentCreate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Create new document.
    """
    document = crud.document.create(db, obj_in=document_in)
    return document

@router.put("/{document_id}", response_model=schemas.Document)
def update_document(
    *,
    db: Session = Depends(deps.get_db),
    document_id: int,
    document_in: schemas.DocumentUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Update a document.
    """
    document = crud.document.get(db, id=document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    document = crud.document.update(db, db_obj=document, obj_in=document_in)
    return document

@router.get("/{document_id}", response_model=schemas.Document)
def read_document_by_id(
    *,
    db: Session = Depends(deps.get_db),
    document_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get a specific document by ID.
    """
    document = crud.document.get(db, id=document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@router.delete("/{document_id}", response_model=schemas.Document)
def delete_document(
    *,
    db: Session = Depends(deps.get_db),
    document_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Delete a document.
    """
    document = crud.document.get(db, id=document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    document = crud.document.remove(db, id=document_id)
    return document

