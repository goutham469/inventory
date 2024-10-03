import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="goutham.sql",
    database="inventory"
)
cursor = connection.cursor()

data = """
insert into customers (customer_name, phone_number, address)
values('raju','9398141936','1-72/1,madhapuram,khammam')
"""
cursor.execute(data)
connection.commit()

cursor.close()
connection.close()
