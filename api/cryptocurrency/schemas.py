from typing import Optional, List
from pydantic import BaseModel, validator


class CryptoCurrencySchemas(BaseModel):
    api_id: Optional[int] = None
    name: Optional[str] = None
    rank: Optional[int] = None
    symbol: Optional[str] = None
    url: Optional[str] = None
    contracts: List
    image: Optional[str] = None
    explorers: Optional[List[str]] = None
    wallets: Optional[List[str]] = None
    community: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    market_id: Optional[int]
