from typing import Optional

from pydantic import BaseModel

from app.schemas.base import MetaData

class DocumentBase(BaseModel):
    filename: str
    file_path: str
    file_type: str

class DocumentCreate(DocumentBase):
    pass

class DocumentUpdate(DocumentBase):
    filename: Optional[str] = None
    file_path: Optional[str] = None
    file_type: Optional[str] = None

class DocumentInDBBase(DocumentBase, MetaData):
    id: Optional[int] = None

    class Config:
        from_attributes = True

class Document(DocumentInDBBase):
    pass

