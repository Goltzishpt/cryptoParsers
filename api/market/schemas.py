from pydantic import BaseModel


class MarketSchemas(BaseModel):
    name: str
    url: str


