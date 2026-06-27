from fastapi import HTTPException
from repositories.get_a_book_by_id import get_a_book_by_id_from_db
from repositories.update_book import update_book_by_id_from_db
from schemas.response_validation import Books_response_validation


def update_book_by_id_service(
    book_id: int, item: dict[str, any]
) -> Books_response_validation:
    old_item = get_a_book_by_id_from_db(book_id)
    if old_item is None:
        raise HTTPException(
            status_code=404, detail=f"the {book_id} is not successfully found"
        )

    update_book = {**old_item, **item}

    saved_book = update_book_by_id_from_db(book_id, update_book)

    return Books_response_validation.model_validator(saved_book)
