from fastapi import APIRouter

from schemas.response_validation import Books_response_validation
from schemas.request_validation import Books_request_validation
from services.get_books import all_books_service
from services.get_book_by_id import get_a_book_by_id_service
from services.create_book import create_book_service
from services.update_book import update_book_by_id_service
from services.delete_book_by_id import delete_book_by_id_service



router = APIRouter(prefix="/books",tags=["Books"])

@router.get("/")
def get_all_books():
    return all_books_service()

@router.get("/{book_id}")
def get_book_by_id(book_id:int):
    return get_a_book_by_id_service(book_id)

@router.post("/",response_model=Books_response_validation)
def create_book(book:Books_request_validation):
    return create_book_service(book)

@router.patch("/{book_id}")
def update_book(book_id:int,data:dict):
    return update_book_by_id_service(book_id,data)

@router.delete("/{book_id}")
def delete_book(book_id:int):
    return delete_book_by_id_service(book_id)



