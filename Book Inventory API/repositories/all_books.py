from integrations.db import get_db_connection


def get_all_books_from_db() -> list[dict]:
    query = "SELECT * FROM books"

    connection = get_db_connection()
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()  # list of tuples
                columns = [desc[0] for desc in cursor.description]
                books = [dict(zip(columns, row)) for row in rows]
                return books
    finally:
        connection.close()
