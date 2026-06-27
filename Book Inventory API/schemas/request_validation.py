from decimal import Decimal

from pydantic import BaseModel


class Books_request_validation(BaseModel):
    title: str
    author: str
    price: Decimal
    quantity: int
