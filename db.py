import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="backend_database"
)

cursor = connection.cursor()