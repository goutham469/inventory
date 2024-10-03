import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="goutham.sql",
    database="inventory"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# SQL commands to create the tables, insert customer data, and insert purchase data
create_customers_table = """
    CREATE TABLE Customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(50),
        phone_number VARCHAR(20),
        address VARCHAR(100)
    )
"""

create_purchases_table = """
    CREATE TABLE Purchases (
        purchase_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        product_name VARCHAR(100),
        quantity INT,
        price DECIMAL(10, 2),
        total_bill DECIMAL(10, 2),
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
"""

insert_customer_data = """
    INSERT INTO Customers (customer_name, phone_number, address)
    VALUES ('Goutham', '12345688', '12-5/2, Melbourne')
"""

# Execute the SQL commands
cursor.execute(create_customers_table)
cursor.execute(create_purchases_table)
cursor.execute(insert_customer_data)

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()
