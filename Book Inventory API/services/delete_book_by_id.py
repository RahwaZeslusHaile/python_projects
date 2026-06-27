from fastapi import HTTPException
from repositories.delete_book import delete_book_by_id_from_db


def delete_book_by_id_service(book_id: int) -> dict[str, str]:
    is_deleted = delete_book_by_id_from_db(book_id)
    if not is_deleted:
        raise HTTPException(
            status_code=404, detail=f"the {book_id} is not successfully deleted"
        )

    else:
        return {"message": f"the {book_id} is successfully deleted"}
