from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.ServiceType])
def read_service_types(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve service types.
    """
    service_types = crud.service_type.get_multi(db, skip=skip, limit=limit)
    return service_types

@router.post("/", response_model=schemas.ServiceType)
def create_service_type(
    *,
    db: Session = Depends(deps.get_db),
    service_type_in: schemas.ServiceTypeCreate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Create new service type.
    """
    service_type = crud.service_type.create(db, obj_in=service_type_in)
    return service_type

@router.put("/{service_type_id}", response_model=schemas.ServiceType)
def update_service_type(
    *,
    db: Session = Depends(deps.get_db),
    service_type_id: int,
    service_type_in: schemas.ServiceTypeUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Update a service type.
    """
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
    """
    Get a specific service type by ID.
    """
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
    """
    Delete a service type.
    """
    service_type = crud.service_type.get(db, id=service_type_id)
    if not service_type:
        raise HTTPException(status_code=404, detail="Service type not found")
    service_type = crud.service_type.remove(db, id=service_type_id)
    return service_type

