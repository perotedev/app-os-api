
from datetime import datetime
from typing import Optional, Generic, TypeVar, List

from pydantic import BaseModel, conint

T = TypeVar("T")

class MetaData(BaseModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class PageParams(BaseModel):
    page: conint(ge=1) = 1
    size: conint(ge=1, le=100) = 10

class PaginationResponse(BaseModel, Generic[T]):
    page: int
    size: int
    total: int
    total_pages: int
    items: List[T]
