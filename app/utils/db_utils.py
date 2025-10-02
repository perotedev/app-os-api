
from pydantic import BaseModel
from enum import Enum
from app.schemas.base import PageParams
from math import ceil
from typing import Dict, Any

class DbUtils:
    def update_entity_fields(self,entity, update_data:dict):
        for field, value in update_data.items():
            if not isinstance(value,Enum):
                setattr(entity, field, value)
            else:
                setattr(entity, field, value.value)
            
    def paginate(self, page_params: PageParams, query) -> Dict[str, Any]:
        offset = (page_params.page - 1) * page_params.size
        paginated_query = query.offset(offset).limit(page_params.size)
                
        res = paginated_query.all()
        total=query.count()
        total_pages = ceil(total / page_params.size) if page_params.size else 1

        data_res = {
            "total": total,
            "page": page_params.page,
            "size": page_params.size,
            "total_pages": total_pages,
            "items": res
        }
        return data_res
    
db_utils = DbUtils()