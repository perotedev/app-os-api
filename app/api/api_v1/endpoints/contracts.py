from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.schemas.base import PaginationResponse, PageParams

router = APIRouter()

@router.get("/", response_model=PaginationResponse[schemas.ContractResume])
def read_contracts(
    page_params: PageParams = Depends(),
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    contracts = crud.contract.get_multi_paginated(db, page_params)
    return contracts

@router.post("/", response_model=schemas.ContractResume)
def create_contract(
    *,
    db: Session = Depends(deps.get_db),
    contract_in: schemas.ContractCreate,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    contract = crud.contract.create(db, obj_in=contract_in)
    return contract

@router.put("/{contract_id}", response_model=schemas.Contract)
def update_contract(
    *,
    db: Session = Depends(deps.get_db),
    contract_id: int,
    contract_in: schemas.ContractUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    contract = crud.contract.get(db, id=contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    contract = crud.contract.update(db, db_obj=contract, obj_in=contract_in)
    return contract

@router.get("/{contract_id}", response_model=schemas.Contract)
def read_contract_by_id(
    *,
    db: Session = Depends(deps.get_db),
    contract_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    contract = crud.contract.get(db, id=contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    return contract

@router.delete("/{contract_id}", response_model=schemas.Contract)
def delete_contract(
    *,
    db: Session = Depends(deps.get_db),
    contract_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    contract = crud.contract.get(db, id=contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    contract = crud.contract.remove(db, id=contract_id)
    return contract

