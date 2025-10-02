from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.schemas.base import PageParams, PaginationResponse

router = APIRouter()

@router.get("/", response_model=PaginationResponse[schemas.ServiceType])
def read_service_types(
    page_params: PageParams = Depends(),
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    service_types = crud.service_type.get_multi_paginated(db, page_params)
    return service_types

@router.post("/", response_model=schemas.ServiceType)
def create_service_type(
    *,
    db: Session = Depends(deps.get_db),
    service_type_in: schemas.ServiceTypeCreate,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    service_type = crud.service_type.create(db, obj_in=service_type_in)
    return service_type

@router.put("/{service_type_id}", response_model=schemas.ServiceType)
def update_service_type(
    *,
    db: Session = Depends(deps.get_db),
    service_type_id: int,
    service_type_in: schemas.ServiceTypeUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    service_type = crud.service_type.get(db, id=service_type_id)
    if not service_type:
        raise HTTPException(status_code=404, detail="Service type not found")
    service_type = crud.service_type.update(db, db_obj=service_type, obj_in=service_type_in)
    return service_type

@router.get("/{service_type_id}", response_model=schemas.ServiceType)
def read_service_type_by_id(
    *,
    db: Session = Depends(deps.get_db),
    service_type_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    service_type = crud.service_type.get(db, id=service_type_id)
    if not service_type:
        raise HTTPException(status_code=404, detail="Service type not found")
    return service_type

@router.delete("/{service_type_id}", response_model=schemas.ServiceType)
def delete_service_type(
    *,
    db: Session = Depends(deps.get_db),
    service_type_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    service_type = crud.service_type.get(db, id=service_type_id)
    if not service_type:
        raise HTTPException(status_code=404, detail="Service type not found")
    service_type = crud.service_type.remove(db, id=service_type_id)
    return service_type

