from decimal import Decimal

from pydantic import BaseModel


class Books_request_validation(BaseModel):
    title: str
    author_id: int
    price: Decimal
    quantity: int
