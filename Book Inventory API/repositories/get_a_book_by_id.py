from integrations.db import get_db_connection


def get_a_book_by_id_from_db(book_id: int) -> dict | None:
    query = "SELECT * FROM books WHERE book_id = %s"

    connection = get_db_connection()
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (book_id,))
                row = cursor.fetchone()
                if row is None:
                    return None
                columns = [desc[0] for desc in cursor.description]
                book = dict(zip(columns, row))
                return book
    finally:
        connection.close()
