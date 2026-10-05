import mysql.connector

try:
    with mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="office_db"
    ) as conn:

        with conn.cursor() as cursor:

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL UNIQUE,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    employee_id INT NOT NULL UNIQUE,
                    salary INT NOT NULL,
                    country VARCHAR(255) NULL
                )
            """)

            cursor.execute("""
                INSERT IGNORE INTO employee
                (name, email, employee_id, salary, country)
                VALUES
                    ('Faruk', 'faruk@example.com', 101, 10000, 'Bangladesh'),
                    ('Ahmed', 'ahmed@example.com', 102, 12000, 'Bangladesh'),
                    ('Jay', 'jay@example.com', 103, 14000, 'India'),
                    ('Mina', 'mina@example.com', 104, 16000, 'India')
            """)

            conn.commit()

            print("Data inserted successfully!")

            cursor.execute("SELECT * FROM employee")

            rows = cursor.fetchall()

            for row in rows:
                print(row)

except mysql.connector.Error as err:
    print("Error:", err)