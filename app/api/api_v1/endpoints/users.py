
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.schemas.base import PageParams, PaginationResponse

router = APIRouter()

@router.get("/", response_model=PaginationResponse[schemas.UserResume])
def read_users(
    page_params: PageParams = Depends(),
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    users = crud.user.get_multi_paginated(db, page_params)
    return users

@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    # First create the person
    person = crud.person.create(db, obj_in=user_in.person)
    # Then create the user, linking to the person
    user = crud.user.create(db, obj_in=user_in)
    # Create default user config
    crud.user_config.create(db, obj_in=schemas.UserConfigCreate(user_id=user.id))
    return user

@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: schemas.UserUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user_in.person:
        crud.person.update(db, db_obj=user.person, obj_in=user_in.person)
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user

@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    current_user: schemas.User = Depends(deps.get_current_active_admin),
) -> Any:
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = crud.user.remove(db, id=user_id)
    return user

@router.put("/user-config/{config_id}", response_model=schemas.UserConfig)
def update_user_config(
    *,
    db: Session = Depends(deps.get_db),
    config_id: int,
    user_config: schemas.UserConfigUpdate,
    current_user: schemas.User = Depends(deps.get_current_active_user),
) -> Any:
    current_config = crud.user_config.get(db, id=config_id)
    if not user_config:
        raise HTTPException(status_code=404, detail="User config not found")
    current_config = crud.user.update(db, db_obj=current_config, obj_in=user_config)
    return current_config