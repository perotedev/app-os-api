
from datetime import datetime
from typing import Optional, Generic, TypeVar, List

from pydantic import BaseModel, Field

T = TypeVar("T")

class MetaData(BaseModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class PaginationResponse(BaseModel, Generic[T]):
    total: int
    page: int
    size: int
    items: List[T]


