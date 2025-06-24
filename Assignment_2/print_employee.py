import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "Sourya@0145",
    database = "sourabh"
)

query = f"select * from employee;"

cursor = connection.cursor()

cursor.execute(query)

employees = cursor.fetchall()

for e in employees:
    print(e)

cursor.close()

connection.close()