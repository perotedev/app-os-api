
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Person])
def read_persons(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve persons.
    """
    persons = crud.person.get_multi(db, skip=skip, limit=limit)
    return persons

@router.post("/", response_model=schemas.Person)
def create_person(
    *,
    db: Session = Depends(deps.get_db),
    person_in: schemas.PersonCreate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Create new person.
    """
    person = crud.person.create(db, obj_in=person_in)
    return person

@router.put("/{person_id}", response_model=schemas.Person)
def update_person(
    *,
    db: Session = Depends(deps.get_db),
    person_id: int,
    person_in: schemas.PersonUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Update a person.
    """
    person = crud.person.get(db, id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    person = crud.person.update(db, db_obj=person, obj_in=person_in)
    return person

@router.get("/{person_id}", response_model=schemas.Person)
def read_person_by_id(
    *,
    db: Session = Depends(deps.get_db),
    person_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get a specific person by ID.
    """
    person = crud.person.get(db, id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@router.delete("/{person_id}", response_model=schemas.Person)
def delete_person(
    *,
    db: Session = Depends(deps.get_db),
    person_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Delete a person.
    """
    person = crud.person.get(db, id=person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    person = crud.person.remove(db, id=person_id)
    return person

