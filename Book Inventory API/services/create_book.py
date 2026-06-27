from datetime import datetime, timezone
from uuid import uuid4

from schemas.request_validation import Books_request_validation
from schemas.response_validation import Books_response_validation


def create_book(books: Books_request_validation) -> Books_response_validation:
    new_book = books.model_dump()
    new_book["id"] = str(uuid4())
    new_book["created_at"] = datetime.now(timezone.utc)

    return Books_response_validation(**new_book)
