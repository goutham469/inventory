import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="goutham.sql",
    database="inventory"
)
#conn = connection.cursor()

# Specify the table name you want to check
table_name = 'customers'

# Connect to the MySQL database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Use a SQL query to check if the table exists
    query = "SHOW TABLES LIKE %s"
    cursor.execute(query, (table_name,))

    # Fetch the result
    result = cursor.fetchone()

    # Check if the table exists
    if result:
        print("The table '{}' exists.".format(table_name))
    else:
        print("The table '{}' does not exist.".format(table_name))
        
except mysql.connector.Error as err:
    print("Error: {}".format(err))

finally:
    if conn:
        print("table exists")
    else :
        print("table does not exists")
