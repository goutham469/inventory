import tkinter as tk
import os
import datetime
import csv
import billing as billing

global_l=[]
p=0
def customer_purchase_data_base(s):
    clock = datetime.datetime.now()
    date = clock.date()
    time = clock.strftime("%H%M%S")
    s.append(date)
    file_name = "customer wise purchases.csv"
    if os.path.exists(file_name) :
        with open (file_name,"a")as file:
            writer = csv.writer(file)
            writer.writerow(s)
    else :
        with open (file_name,'w')as file :
            writer =csv.writer(file)
            l=[]
            l.append("Name")
            l.append("Phone")
            l.append("Product")
            l.append("Items")
            l.append("Bill")
            l.append("Date")
            l.append("Time")
            writer.writerow(l)
            writer.writerow(s)
            
            
# functions here
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
        s=global_l
        #s.append(name_entry.get())
        #s.append(phone_entry.get())
        #s.append(global_l[])
        #s.append()
        #s.append()
        #s.append()
        print("total bill = ",p)
        file_name=name_entry.get()
        file_name+=".txt"
        
        with open(file_name,"w") as file :
         #customer_purchase_data_base(s)
        # come to above module only after capable of working with mySQL
        # efficient data base is required 
            file.write("\t\t\tname : ")
            file.write(name_entry.get())
            file.write("\n\n\n")
            file.write("\tItem\t\tPrice\t\tQuantity\n\n\n")
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
            file.write(" Rs/-")
            file.close()
            
                
            
        print("bill saved as word document")
        
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

print("you are inside main module")
#create main window
root=tk.Tk()
root.geometry("500x500")
root.title("inventory")

#creating labels
main_title = tk.Label(root,text="Inventory management ")
name = tk.Label(root,text="Name ")
password = tk.Label(root, text="Password")

#creating input entry fields
name_entry = tk.Entry(root)
password_entry = tk.Entry(root)

#creating buttons
billing_button = tk.Button(root,text="Billing",command=bill)
add_stock_button = tk.Button(root,text="add stock",command=add_stock)
report_button = tk.Button(root,text="Report", command=report)
exit_button = tk.Button(root,text="exit",command=exit1)

#arranging buttons and labels in grid system
main_title.grid(row = 0, column=0 , columnspan=2)
name.grid(row=1,column=0)
name_entry.grid(row=1,column=1)
password.grid(row=2,column=0)
password_entry.grid(row=2,column=1)
billing_button.grid(row=3 ,column=0,columnspan=2)
add_stock_button.grid(row=4 ,column=0,columnspan=2)
report_button.grid(row=5 ,column=0,columnspan=2)
exit_button.grid(row=6 ,column=0,columnspan=2)

root.mainloop()

