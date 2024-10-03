import os

def customer_id_get():
    file_name = "customer_unique_id.txt"
    
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = file.read()
            value = int(data) + 1
        with open(file_name, "w") as file:
            file.write(str(value))
    else:
        with open(file_name, "w") as file:
            value = 1
            file.write(str(value))
    
    return value

print(customer_id_get())
