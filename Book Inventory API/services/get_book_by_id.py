from fastapi import HTTPException
from repositories.get_a_book_by_id import get_a_book_from_db
from schemas.response_validation import Books_response_validation


def gt_a_book_by_id_service(book_id) -> Books_response_validation:

    raw_book = get_a_book_from_db(book_id)
    if raw_book is None:
        return Books_response_validation.model_validate(raw_book)
    else:
        raise HTTPException(status_code=404, detail="book not found")
