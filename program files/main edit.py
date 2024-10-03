import tkinter as tk
import billing as billing
import mysql.connector
import os

global_l=[]
p=0
# functions here
def customer_id_get():
    file_name = "customer_unique_id.txt"
    if os.path.exists (file_name) :
        with open (file_name,"r") as file :
            data = file.read()
            value = int(data) + 1
        with open (file_name,"w") as file :
            file.write(str(value))
    else :
        with open(file_name,"w")as file :
            value = 1
            file.write(str(value))
            
    return value
def product_id_get():
    file_name = "product_unique_id.txt"
    if os.path.exists (file_name) :
        with open (file_name,"r") as file :
            data = file.read()
            value = int(data) + 1
        with open (file_name,"w") as file :
            file.write(str(value))
    else :
        with open(file_name,"w")as file :
            value = 1
            file.write(str(value))
            
    return value
def save_database(s):
    global p
    # input for this function is a list
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "goutham.sql",
        database = "inventory"
        )
    cursor = connection.cursor()
    id_num = customer_id_get()

    data ="""
insert into customers(customer_id,customer_name,phone_number,address,total_bill)
values(%s,%s,%s,%s,%s)
"""
    cursor.execute(data,(id_num,s[0],s[1],"not available",p))
    data = """
insert into purchases(purchase_id,customer_id,product_name,quantity,price,total_bill)
values(%s,%s,%s,%s,%s,%s)
"""
    for i in s[2] :
        #iterate over purchase items
        
        cursor.execute(data,(product_id_get(),id_num,i[0],i[1],i[2],i[2]*i[1]))
    print("data entered to data base ")
 
    connection.commit()
    cursor.close()
    connection.close()
    

    
def create_tables():
    def customers():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="goutham.sql",
            database="inventory"
            )
        
        cursor = connection.cursor()
        create_customers_table ="""
        CREATE TABLE Customers
        (
        customer_id INT ,
        customer_name VARCHAR(50),
        phone_number VARCHAR(20),
        address VARCHAR(100),
        total_bill DECIMAL(10,3)
        )
        """
        
        create_purchases_table ="""
        CREATE TABLE Purchases
        (
        purchase_id INT,
        customer_id INT,
        product_name VARCHAR(100),
        quantity INT,
        price DECIMAL(10, 3),
        total_bill DECIMAL(10, 3)
        )
        """
        cursor.execute(create_customers_table)
        cursor.execute(create_purchases_table)
        
        connection.commit()
        cursor.close()
        connection.close()
    # calling customers function to create tables
    customers()
def get_customer_details():
    def next():
        l=[]
        l.append(name_entry.get())
        l.append(phone_entry.get())
        l.append(addr_entry.get())
        l.append(email_entry.get())
        print(l)
    l=[]
    Child = tk.Toplevel(root)
    Child.geometry("500x500")
    Child.title("customer details")

    #labels
    des=tk.Label(Child,text="please enter customer details",fg="red")
    name_label = tk.Label(Child,text="name")
    phone_label=tk.Label(Child,text="phone")
    addr_label=tk.Label(Child,text="address")
    email_label=tk.Label(Child,text="email")

    #buttons
    next_button=tk.Button(Child,text="next",width=10,height=2,command=next)

    #entry fields
    name_entry = tk.Entry(Child)
    phone_entry = tk.Entry(Child)
    addr_entry = tk.Entry(Child)
    email_entry = tk.Entry(Child)

    #grid layout
    des.grid(row=0,column=0,columnspan=2)
    name_label.grid(row=1,column=0)
    name_entry.grid(row=1 ,column=1 )
    phone_label.grid(row=2 ,column=0 )
    phone_entry.grid(row=2 ,column=1 )
    addr_label.grid(row=3 ,column=0 )
    addr_entry.grid(row=3 ,column=1 )
    email_label.grid(row=4 ,column=0 )
    email_entry.grid(row=4 ,column=1 )
    next_button.grid(row=5 ,column=0,columnspan=2)

      
def bill():
    
    global global_l
    global p
    global_l=[]
    p=0
    billitem()
    # print("after calling billitem ",global_l)
    # for i in global_l:
     #   print(i)
     #   p+=i[1]*i[2]
    # print("bill generated amount = ",p)




    
    
# originally written by me    
def billitem():
    
    print("in the bill menu module")
    
    def clear_name():
        name_entry.delete(0,tk.END)
    def clear_phone():
        phone_entry.delete(0,tk.END)
    def clear1():
        product_name_entry.delete(0,tk.END)
    def clear2():
        price_entry.delete(0,tk.END)
    def clear3():
        quantity_entry.delete(0,tk.END)
    def clear_all():
        clear1()
        clear2()
        clear3()
    def submit():
        print("submit")
        
    def save():
        global global_l
        global p
        p=0
        for i in global_l:
            p+=i[1]*i[2]
        print("total bill = ",p)
        file_name=name_entry.get()
        file_name+=".txt"
        
        with open(file_name,"w") as file :
            file.write("\t\t\tname : ")
            file.write(name_entry.get())
            file.write("\n\n\n")
            file.write("\tItem\t\t\tPrice\t\t\tQuantity\n\n\n")
            c=1
            for i in global_l :
                file.write(str(c))
                file.write("\t")
                file.write(str(i[0]))
                file.write("\t")
                file.write(str(i[1]))
                file.write("\t")
                file.write(str(i[2]))
                file.write("\t")
                file.write(str(i[1]*i[2]))
                file.write("\n\n")
            file.write("Total Bill = ")
            file.write(str(p))
            file.close()
        #sending global_l data list and customer details to data base
            a=[]
            a.append(name_entry.get())
            a.append(phone_entry.get())
            # appending purchase details
            a.append(global_l)
            a.append(p)  
        print("bill saved as word document")
        save_database(a)
        print("customer data saved to data base")
        
    def next_item():
        global global_l
        name = product_name_entry.get()
        
        try :
            price = float(price_entry.get())
        except ValueError :
            bill.config(text="enter a valid value for price")
        #this entry should be a float
        try :
            quantity = int(quantity_entry.get())
        except ValueError :
            bill.config(text="enter a valid value for quantity")
        
        
        
        l=[]
        l.append(name)
        l.append(price)
        l.append(quantity)
        # print(l)
     
        global_l.append(l)
        print("appending ",l[0]," complete"," list ",global_l)
        clear_all()
        

    print("you are inside billing module")
    bill_items_details=[]

    child_window = tk.Toplevel(root)
    child_window.title("billing module")
    child_window.geometry("300x1000")

    #label creation

    customer_name = tk.Label(child_window, text="name")
    phone_number = tk.Label(child_window, text="phone")
    Billing = tk.Label(child_window,text="Billing")
    product_name =tk.Label(child_window,text="Product")
    price = tk.Label(child_window,text="Price")
    quantity = tk.Label(child_window,text="Quantity")
    bill = tk.Label(child_window,text="warnings")
    
    

    #entry field

    name_entry = tk.Entry(child_window)
    phone_entry = tk.Entry(child_window)
    product_name_entry = tk.Entry(child_window)
    price_entry = tk.Entry(child_window)
    quantity_entry = tk.Entry(child_window)
    

    #buttons field
    clear_name_button = tk.Button(child_window,text="Clear",command=clear_name)
    clear_phone_button = tk.Button(child_window,text="Clear",command=clear_phone)
    clear1_button = tk.Button(child_window,text="Clear",command=clear1)
    clear2_button = tk.Button(child_window,text="Clear",command=clear2)
    clear3_button = tk.Button(child_window,text="Clear",command=clear3)
    clear_all_button = tk.Button(child_window,text="Clear",command=clear_all)
   # submit_button = tk.Button(root,text="Submit",command=submit)
    save_button = tk.Button(child_window,text="Save",command=save)
    next_button = tk.Button(child_window,text="next",command=next_item)
    
    
    
    #grid layout

    customer_name.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    clear_name_button.grid(row=0,column=2)
    
    phone_number.grid(row=1,column=0)
    phone_entry.grid(row=1,column=1)
    clear_phone_button.grid(row=1,column=2)
    Billing.grid(row=2,column=0,columnspan=2)
    
    product_name.grid(row=3 ,column=0 )
    product_name_entry.grid(row=3 ,column=1 ,padx=10)
    clear1_button.grid(row=3 ,column=2)
    
    price.grid(row=4 ,column=0 )
    price_entry.grid(row=4 ,column=1 )
    clear2_button.grid(row=4 ,column=2)
    
    quantity.grid(row=5 ,column=0 )
    quantity_entry.grid(row=5 ,column=1 )
    clear3_button.grid(row=5 ,column=2)
    
    clear_all_button.grid(row=6 ,column=0)
  #  submit_button.grid(row=6 ,column=1)
    next_button.grid(row=6 ,column=2)
    
    save_button.grid(row=7 ,column=0,columnspan=3)
    bill.grid(row=8 ,column=0 ,columnspan=3)

    # return global_l


    
    
def add_stock():
    print("over")
def report():
    print("over")
def exit1():
    print("thank you")
    exit()
def settings():
    print("settings tab called")


def main():
    print("you are inside main module")
    
    #create_tables()
    main_window=tk.Toplevel(root)
    main_window.geometry("500x500")
    main_window.title("inventory")

    #creating labels
    main_title = tk.Label(main_window,text="Inventory management ")
    name = tk.Label(main_window,text="Name ")
    password = tk.Label(main_window, text="Password")


    #creating buttons
    billing_button = tk.Button(main_window,text="Billing",command=bill)
    add_stock_button = tk.Button(main_window,text="add stock",command=add_stock)
    report_button = tk.Button(main_window,text="Report", command=report)
    exit_button = tk.Button(main_window,text="exit",command=exit1)
    sett = tk.Button(main_window,text="Settings",command=settings)

    #arranging buttons and labels in grid system
    main_title.grid(row = 0, column=0 , columnspan=2)
    name.grid(row=1,column=0,columnspan=2)
    password.grid(row=2,column=0,columnspan=2)
    billing_button.grid(row=3 ,column=0,columnspan=2)
    add_stock_button.grid(row=4 ,column=0,columnspan=2)
    report_button.grid(row=5 ,column=0,columnspan=2)
    sett.grid(row=6,column=0,columnspan=2)
    exit_button.grid(row=7 ,column=0,columnspan=2)




#                      main program  for user  credentials 



def submit():
    name = user_name_entry.get()
    password = password_entry.get()
    with open("passwords.txt","r")as file:
        data = file.read()
        data = data.split("\n")
        u = data[0]
        p = data[1]
        if (u == name ):
            if (p == password):
                print("success you can call main code")
                main()
            else :
                messages.config(text="messages\nInvalid Password",fg="red")
        else :
            messages.config(text="messages\nInvalid user name",fg="red")
def forgot():
    messages.config(fg="green",text="messages\nwhat is your\nfavourate food ?\nenter answer in user name")
root= tk.Tk()
root.geometry("200x200")
root.title("credentials")

# creating labels
wisher = tk.Label(root,text="Welcome To Inventory Management")
user_name = tk.Label(root,text="user name")
password = tk.Label(root,text="password")
messages = tk.Label(root,text="messages")

#creating entry fields

user_name_entry = tk.Entry(root)
password_entry = tk.Entry(root)

#buttons
submit_button = tk.Button(root,text="Submit",command=submit)
forgot_password_button = tk.Button(root,text="Forgot",command = forgot)

#grid layout setup
wisher.grid(row =0 ,column =0 ,columnspan=2 )
user_name.grid(row =1 ,column =0  )
user_name_entry.grid(row =1 ,column = 1 )
password.grid(row =2 ,column =0  )
password_entry.grid(row =2 ,column = 1 )
forgot_password_button.grid(row=3,column=0)
submit_button.grid(row =3 ,column = 1 )
messages.grid(row=4,column=0,columnspan=2)


root.mainloop()
