import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "goutham.sql",
    database = "inventory"
    )
cursor = connection.cursor()
l=[]
l.append("realme 5i")
l.append(5)
l.append(9999.9)
l.append(99999)

a=[]
for i in range(3):
    a.append(l)


data = """
insert into purchases (product_name,quantity,price,total_bill)
values(%s,%s,%s,%s)
"""
for i in a :
    cursor.execute(data,(i[0],i[1],i[2],i[3]))

connection.commit()

cursor.close()
connection.close()
