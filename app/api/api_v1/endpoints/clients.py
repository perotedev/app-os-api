
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.base import PaginationResponse, PageParams

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=PaginationResponse[schemas.Client])
def read_clients(
    page_params: PageParams = Depends(),
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    clients = crud.client.get_multi_paginated(db, page_params)
    return clients

@router.post("/", response_model=schemas.Client)
def create_client(
    *,
    db: Session = Depends(deps.get_db),
    client_in: schemas.ClientCreate,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    client = crud.client.create(db, obj_in=client_in)
    return client

@router.put("/{client_id}", response_model=schemas.Client)
def update_client(
    *,
    db: Session = Depends(deps.get_db),
    client_id: int,
    client_in: schemas.ClientUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
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
    client = crud.client.get(db, id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    client = crud.client.remove(db, id=client_id)
    return client

