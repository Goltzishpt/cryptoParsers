from typing import Optional, List

from pydantic import BaseModel, validator


class ContractsSchemas(BaseModel):
    name: Optional[str] = None
    contract_address: Optional[str] = None
    chain_id: Optional[int] = None
    decimal: Optional[int] = None
    image: Optional[str] = None
    cryptocurrency_id: Optional[int] = None

    # @validator('cryptocurrency_id', pre=True, always=True)
    # def check_crypto_id(self, value):
    #     if value is None:
    #         raise ValueError("cryptocurrency_id must be provided")
    #     return value
