from integrations.db import get_db_connection
def update_book_by_id_from_db(book_id:int,data:dict)->dict|None:
    data = {k: v for k, v in data.items() if k!= book_id}
    if not data:
        return None
    set_parts = []
    values = []
    for key,value in data.items():
        set_parts.append(f"{key} = %s")
        values.append(value)
    set_clause = ", ".join(set_parts)
    query = f"""
            UPDATE  books 
            SET {set_clause}
            WHERE book_id = %s
    """
    values.append(book_id)
    
    connection = get_db_connection()
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query,values)
                if cursor.rowcount == 0:
                    return None
                cursor.execute(
                    "SELECT * FROM books WHERE book_id = %s",
                    (book_id,)
                )
                row = cursor.fetchone()
                if row is None:
                    return None
                column= [desc[0] for desc in cursor.description]
                return dict(zip(column,row))
    finally:
        connection.close()
