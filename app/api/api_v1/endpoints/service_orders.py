
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.schemas.base import PageParams, PaginationResponse

router = APIRouter()

@router.get("/", response_model=PaginationResponse[schemas.ServiceOrderResume])
def read_service_orders(
    page_params: PageParams = Depends(),
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    service_orders = crud.service_order.get_multi_paginated(db, page_params)
    return service_orders

@router.post("/", response_model=schemas.ServiceOrder)
def create_service_order(
    *,
    db: Session = Depends(deps.get_db),
    service_order_in: schemas.ServiceOrderCreate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Create new service order.
    """
    service_order = crud.service_order.create(db, obj_in=service_order_in)
    return service_order

@router.put("/{service_order_id}", response_model=schemas.ServiceOrder)
def update_service_order(
    *,
    db: Session = Depends(deps.get_db),
    service_order_id: int,
    service_order_in: schemas.ServiceOrderUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Update a service order.
    """
    service_order = crud.service_order.get(db, id=service_order_id)
    if not service_order:
        raise HTTPException(status_code=404, detail="Service order not found")
    service_order = crud.service_order.update(db, db_obj=service_order, obj_in=service_order_in)
    return service_order

@router.get("/{service_order_id}", response_model=schemas.ServiceOrder)
def read_service_order_by_id(
    *,
    db: Session = Depends(deps.get_db),
    service_order_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get a specific service order by ID.
    """
    service_order = crud.service_order.get(db, id=service_order_id)
    if not service_order:
        raise HTTPException(status_code=404, detail="Service order not found")
    return service_order

@router.delete("/{service_order_id}", response_model=schemas.ServiceOrder)
def delete_service_order(
    *,
    db: Session = Depends(deps.get_db),
    service_order_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Delete a service order.
    """
    service_order = crud.service_order.get(db, id=service_order_id)
    if not service_order:
        raise HTTPException(status_code=404, detail="Service order not found")
    service_order = crud.service_order.remove(db, id=service_order_id)
    return service_order

