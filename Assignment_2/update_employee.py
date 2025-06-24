import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "Sourya@0145",
    database = "sourabh"
)

empid = 1
name = "professor"
dept = "HR"
salary = 120000
email = "professor@gmail.com"
doj = "18.6.2024"

query = f"update employee SET salary = '{salary}' where empid = {empid};"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()