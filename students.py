from db import cursor, connection

def create_student(name):
    query = "INSERT INTO students (name) VALUES  (%s)"
    cursor.execute(query, (name,))
    connection.commit()