
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
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:

    service_order = crud.service_order.create(db, obj_in=service_order_in)
    return service_order

@router.put("/{service_order_id}", response_model=schemas.ServiceOrder)
def update_service_order(
    *,
    db: Session = Depends(deps.get_db),
    service_order_id: int,
    service_order_in: schemas.ServiceOrderUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:

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

    service_order = crud.service_order.get(db, id=service_order_id)
    if not service_order:
        raise HTTPException(status_code=404, detail="Service order not found")
    service_order = crud.service_order.remove(db, id=service_order_id)
    return service_order

@router.post("/item", response_model=schemas.ServiceOrderItem)
def create_service_order_item(
    *,
    db: Session = Depends(deps.get_db),
    service_order_item_in: schemas.ServiceOrderItemCreate,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:

    so_item = crud.service_order_item.create(db, obj_in=service_order_item_in)
    return so_item

@router.put("/item/{item_id}", response_model=schemas.ServiceOrderItem)
def create_service_order_item(
    *,
    item_id: int,
    db: Session = Depends(deps.get_db),
    service_order_item_in: schemas.ServiceOrderItemUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    so_item = crud.service_order_item.get(db, id=item_id)
    if not so_item:
        raise HTTPException(status_code=404, detail="Service order item not found")
    so_item = crud.service_order_item.update(db, db_obj=so_item, obj_in=service_order_item_in)
    return so_item