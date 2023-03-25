from typing import Optional, List

from pydantic import BaseModel, validator


class ContractsSchemas(BaseModel):
    name: Optional[str] = None
    contract_address: Optional[str] = None
    chain_id: Optional[int] = None
    decimal: Optional[int] = None
    image: Optional[str] = None