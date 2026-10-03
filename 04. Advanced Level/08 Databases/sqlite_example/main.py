import sqlite3

try:
    # create database connection
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        # create table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')
        conn.commit()
        print("Table 'users' created successfully (or already exists).")
        
        # insert data
        cursor.execute('''
            INSERT INTO users (name, age) VALUES ('John Doe', 30)
        ''')
        conn.commit()
        print("Data inserted successfully.")
        
        # update data
        cursor.execute('''
            UPDATE users SET age = 31 WHERE name = 'John Doe'
        ''')
        conn.commit()
        print("Data updated successfully.")
        
        # delete data
        cursor.execute('''
            DELETE FROM users WHERE name = 'John Doe'
        ''')
        conn.commit()
        print("Data deleted successfully.")
        
        # fetch data
        cursor.execute('''
            SELECT * FROM users
        ''')
        rows = cursor.fetchall()
        print("Data fetched successfully.")
        for row in rows:
            print(row)
except sqlite3.Error as e:
    print(f"Database error: {e}")
