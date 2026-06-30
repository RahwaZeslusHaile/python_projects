from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class Books_response_validation(BaseModel):
    book_id: int
    title: str
    author_id: int
    price: Decimal
    quantity: int
    created_at: datetime
