from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Contract])
def read_contracts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve contracts.
    """
    contracts = crud.contract.get_multi(db, skip=skip, limit=limit)
    return contracts

@router.post("/", response_model=schemas.Contract)
def create_contract(
    *,
    db: Session = Depends(deps.get_db),
    contract_in: schemas.ContractCreate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Create new contract.
    """
    contract = crud.contract.create(db, obj_in=contract_in)
    return contract

@router.put("/{contract_id}", response_model=schemas.Contract)
def update_contract(
    *,
    db: Session = Depends(deps.get_db),
    contract_id: int,
    contract_in: schemas.ContractUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Update a contract.
    """
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
    """
    Get a specific contract by ID.
    """
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
    """
    Delete a contract.
    """
    contract = crud.contract.get(db, id=contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    contract = crud.contract.remove(db, id=contract_id)
    return contract

