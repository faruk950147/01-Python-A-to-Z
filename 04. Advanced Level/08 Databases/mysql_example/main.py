import mysql.connector

try:
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="office_db"
    )
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Create a database
    cursor.execute("CREATE DATABASE IF NOT EXISTS office_db")
    
    # Create a table
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

    # Insert data
    cursor.execute("""
        INSERT IGNORE INTO employee (name, email, employee_id, salary, country)
        VALUES 
            ('Faruk', 'faruk@example.com', 101, 10000, 'Bangladesh'),
            ('Ahmed', 'ahmed@example.com', 102, 12000, 'Bangladesh'),
            ('Jay', 'jay@example.com', 103, 14000, 'India'),
            ('Mina', 'mina@example.com', 104, 16000, 'India'),
            ('Charlie Brown', 'charlie@example.com', 105, 18000, 'Germany'),
            ('Diana Prince', 'diana@example.com', 106, 20000, 'France'),
            ('Eve Wilson', 'eve@example.com', 107, 22000, 'Japan'),
            ('James', 'james@example.com', 108, 24000, 'Bangladesh'),
            ('Hasan', 'hasan@example.com', 109, 26000, 'Bangladesh'),
            ('Hafsa', 'hafsa@example.com', 110, 28000, 'Bangladesh')
    """)

    # Commit the transaction
    conn.commit()
    print("Data inserted successfully!")
    
    # Query data
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

except (mysql.connector.Error, Exception) as err:
    print("Error occurred:", err)
