
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Address])
def read_addresses(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    addresses = crud.address.get_multi(db, skip=skip, limit=limit)
    return addresses

@router.post("/", response_model=schemas.Address)
def create_address(
    *,
    db: Session = Depends(deps.get_db),
    address_in: schemas.AddressCreate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    address = crud.address.create(db, obj_in=address_in)
    return address

@router.put("/{address_id}", response_model=schemas.Address)
def update_address(
    *,
    db: Session = Depends(deps.get_db),
    address_id: int,
    address_in: schemas.AddressUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    address = crud.address.get(db, id=address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    address = crud.address.update(db, db_obj=address, obj_in=address_in)
    return address

@router.get("/{address_id}", response_model=schemas.Address)
def read_address_by_id(
    *,
    db: Session = Depends(deps.get_db),
    address_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    address = crud.address.get(db, id=address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

@router.delete("/{address_id}", response_model=schemas.Address)
def delete_address(
    *,
    db: Session = Depends(deps.get_db),
    address_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    address = crud.address.get(db, id=address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    address = crud.address.remove(db, id=address_id)
    return address

