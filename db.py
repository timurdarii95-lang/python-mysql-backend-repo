import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="backend_database"
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(25) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE tasks(
     in INT AUTO_INCREMENT PRIMARY KEY,
     Student_id INT,
     title VARCHAR(255),
     status VARCHAR(20),
     FOREIGN KEY (student_in) REFERENCES students(id)
)
""")

connection.commit()
