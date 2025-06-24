import mysql.connector
def execute_query(query):
    connection=mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="StrongPass123!",
        database="iotdb"
    )
    cursor=connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
def execute_select_query(query):
    connection=mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="StrongPass123!",
        database="iotdb"
    )
    cursor=connection.cursor()
    cursor.execute(query)
    user=cursor.fetchall()
    cursor.close()
    connection.close()
    return user


