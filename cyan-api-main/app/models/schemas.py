from typing import Optional
from pydantic import BaseModel


class Filter(BaseModel):
    price: Optional[str] = None
    price_per_meter: Optional[str] = None
    square: Optional[str] = None
