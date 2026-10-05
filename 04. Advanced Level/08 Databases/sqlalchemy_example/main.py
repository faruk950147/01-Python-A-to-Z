import psycopg

with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="mydatabase",
    user="postgres",
    password="your_password"
) as conn:

    with conn.cursor() as cursor:

        cursor.execute("SELECT * FROM users")

        users = cursor.fetchall()

        for user in users:
            print(user)