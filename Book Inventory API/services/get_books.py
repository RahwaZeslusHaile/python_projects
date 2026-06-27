from repositories.all_books import get_all_books_from_db
from schemas.response_validation import Books_response_validation


def all_books_service(db_session) -> list[Books_response_validation]:
    raw_books = get_all_books_from_db(db_session)

    return [Books_response_validation.model_validate(book) for book in raw_books]
