import pymysql

def get_db_connection():
    return pymysql.connect(
        host = 'localhost',
        port = 8889,
        user = 'root',
        password = 'root',
        database = 'guess_mem'
    )

def get_random_img():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("""select id, correct_answer, card_url from cards 
            order by rand()
            limit 1""")
            return cursor.fetchone()
    except Exception as e:
        print(f"error: {e}")
    finally:
        conn.close()