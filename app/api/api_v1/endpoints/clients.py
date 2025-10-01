
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Client])
def read_clients(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve clients.
    """
    clients = crud.client.get_multi(db, skip=skip, limit=limit)
    return clients

@router.post("/", response_model=schemas.Client)
def create_client(
    *,
    db: Session = Depends(deps.get_db),
    client_in: schemas.ClientCreate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Create new client.
    """
    client = crud.client.create(db, obj_in=client_in)
    return client

@router.put("/{client_id}", response_model=schemas.Client)
def update_client(
    *,
    db: Session = Depends(deps.get_db),
    client_id: int,
    client_in: schemas.ClientUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Update a client.
    """
    client = crud.client.get(db, id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    client = crud.client.update(db, db_obj=client, obj_in=client_in)
    return client

@router.get("/{client_id}", response_model=schemas.Client)
def read_client_by_id(
    *,
    db: Session = Depends(deps.get_db),
    client_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get a specific client by ID.
    """
    client = crud.client.get(db, id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.delete("/{client_id}", response_model=schemas.Client)
def delete_client(
    *,
    db: Session = Depends(deps.get_db),
    client_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Delete a client.
    """
    client = crud.client.get(db, id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    client = crud.client.remove(db, id=client_id)
    return client

