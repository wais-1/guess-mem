import pymysql

def get_db_connection():
    return pymysql.connect(
        host = 'localhost',
        port = 8889,
        user = 'root',
        password = 'root',
        database = 'guess_mem'
    )

# рандом выбор картинки
def get_random_img(used_cards):
    conn = get_db_connection()

    try:
        with conn.cursor() as cursor:
            if used_cards:
                placeholders = ", ".join(["%s"] * len(used_cards)) # для передачи id использованных картинок

                query = f"""
                    SELECT id, correct_answer, card_url
                    FROM cards
                    WHERE id NOT IN ({placeholders})
                    ORDER BY RAND()
                    LIMIT 1
                """

                cursor.execute(query, tuple(used_cards))

            else:
                cursor.execute("""
                    SELECT id, correct_answer, card_url
                    FROM cards
                    ORDER BY RAND()
                    LIMIT 1
                """)

            return cursor.fetchone()

    finally:
        conn.close()