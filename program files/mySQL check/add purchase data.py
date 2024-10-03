import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "goutham.sql",
    database = "inventory"
    )
cursor = connection.cursor()

data = """
insert into purchases (product_name,quantity,price,total_bill)
values('hp 15 s laptop',10,53999.99,539999.9)
"""
cursor.execute(data)

connection.commit()

cursor.close()
connection.close()
