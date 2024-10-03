import tkinter as tk
import billing as billing

# functions here
def bill():
    #a is a list item to hold the data
    l=billitem()
    
        
        

    
def billitem():
    global_l=[]
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
        print("bill saved")
    def next_item():
        global global_l
        name = product_name_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()
        #write a function to check weather the given name , price, quantity are correct or not
        #in case of product name go through the available products if not there delete that entry
        #in case price,quantity take only integer values other input then delete the entry field
        price=int(price)
        quantity=int(quantity)
        l=[]
        l.append(name)
        l.append(price)
        l.append(quantity)
        #create a excel file to write each time purchase of each product so that data will not be lost
        #append the data now read to the existing billing.csv file
        #read all the billing.csv file data as a list into a variable
        #print all the list on the output screen whenever next is pressed
        #after pressing save button generate the total bill and print the "bill amount"
        global_l.append(l)
        #bill.config(text=f"{l[0]}\t{l[1]}\t{l[2]}\t{l[1]*l[2]}\n")
       

    

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
    bill = tk.Label(child_window,text="bill")
    
    

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

    return global_l


    
    
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

