from pydantic import BaseModel
from typing import Optional


class MarketSchemas(BaseModel):
    id: Optional[int]
    name: Optional[str]
    url: Optional[str]
    cryptocurrency_id: Optional[str]
