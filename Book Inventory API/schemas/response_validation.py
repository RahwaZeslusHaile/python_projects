from datetime import datetime
from decimal import Decimal

from pydntic import BaseModel


class Books_response_validation(BaseModel):
    id: str
    title: str
    author: str
    price: Decimal
    quantity: int
    created_at: datetime
