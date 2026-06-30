from integrations.db import get_db_connection

def create_book_in_db(
    title: str,
    author_id:int,
    price,
    quantity:int) -> dict:

    query = """
            INSERT INTO books(title,author_id, price, quantity)
            VALUES(%s,%s,%s,%s)
            RETURNING *

    """
    connection = get_db_connection()

    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query,((title, author_id, price, quantity)))

                row = cursor.fetchone()
                columns = [desc[0] for desc in cursor.description]
                return dict(zip(columns,row))
    finally:
        connection.close()