from integrations.db import get_db_connection


def delete_book_by_id_from_db(book_id: int) -> bool:
    query = "DELETE FROM books WHERE book_id = %s"
    connection = get_db_connection()
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (book_id,))

                return cursor.rowcount > 0

    finally:
        connection.close()
