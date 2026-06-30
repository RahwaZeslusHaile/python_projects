from repositories.create_book import create_book_in_db

from schemas.request_validation import Books_request_validation
from schemas.response_validation import Books_response_validation


def create_book_service(books: Books_request_validation) -> Books_response_validation:
    data = books.model_dump()
    new_book = create_book_in_db(
        title=data["title"],
        author_id=data["author_id"],
        price=data["price"],
        quantity=data["quantity"]
    )

    return Books_response_validation.model_validate(new_book)
