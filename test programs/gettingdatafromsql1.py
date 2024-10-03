import mysql.connector

def get_goods_data():
    connection = mysql.connector.connect(
        host = "localhost",
        user="root",
        password="goutham.sql",
        database="inventory"
    )

    cursor = connection.cursor()

    query = """SELECT * FROM goods"""

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    connection.close()

    for i in data :
        print(i)
def get_purchases_data():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "goutham.sql",
        database = "inventory"
    )

    cursor = connection.cursor()

    query = """SELECT * FROM purchases"""

    cursor.execute(query)

    data = cursor.fetchall()
    cursor.close()
    connection.close()
    for i in data :
        print(i)
        
def get_customers_data():
    connection = mysql.connector.connect()

    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "goutham.sql",
        database = "inventory"
    )

    cursor = connection.cursor()

    query = "select * from customers"

    cursor.execute(query)

    data = cursor.fetchall()
    for i in data :
        print(i)


# get_goods_data()
# get_customers_data()
# get_purchases_data()