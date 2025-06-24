import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "Sourya@0145",
    database = "sourabh"
)

dept = input("enter dept : ")

query = f"select * from employee where dept = '{dept}';"

cursor = connection.cursor()

cursor.execute(query)

employees = cursor.fetchall()

print(employees)

cursor.close()

connection.close()