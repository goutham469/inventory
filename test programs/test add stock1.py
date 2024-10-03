import tkinter as tk
def add_stock():
    print("add_stock")
    # function definitions
    def clear0():
        dealer_entry.delete(0,tk.END)
    def clear1():
        product_entry.delete(0,tk.END)
    def clear2():
        price_entry.delete(0,tk.END)
    def clear3():
        dealer0_entry.delete(0,tk.END)
    def clear4():
        manu_entry.delete(0,tk.END)
    def clear5():
        exp_entry.delete(0,tk.END)
    def clear6():
        quantity_entry.delete(0,tk.END)
    def clear7():
        genre_entry.delete(0,tk.END)
    def clear():
        clear0()
        clear1()
        clear2()
        clear3()
        clear4()
        clear5()
        clear6()
        clear7()
    def check_input_values():
        text_warning = []
        text_warning.append("\n\twarnings\n")
        c = 0
        if (product_entry.get() == ""):
            c=1
            text_warning.append("-->product name\n")
        try :
            price = price_entry.get()
            price = float(price)
        except ValueError :
            c+=1
            text_warning.append("-->price only numeric\n")
        try :
            quantity = int(quantity_entry.get())
        except ValueError :
            c+=1
            text_warning.append("-->quantity only integer\n")
        if manu_entry.get() == "" :
            c+=1
            text_warning.append("-->enter manufacture date\n")
        if exp_entry.get() == "" :
            c+=1
            text_warning.append("-->enter expiry date\n")
        if (genre_entry.get()==""):
            c+=1
            text_warning.append("-->enter genre\n")
        text_warning.append(str(c))
        text_warning.append(" errors occured\n")
        if c == 0 :
            return True
        else :
            l="".join(text_warning)
            warnings_label.config(text=l,fg="red",font="20px")
            return False
    def calculate_bill():
        global add_stock_details 
        if len(add_stock_details) != 0 :
            s = 0
            a = []
            a.append("Total = ")
            for i in add_stock_details :
                s+=i[1]*i[5]
                a.append(str(s))
            a="".join(a)
            total_label.config(text=a,fg="brown",font="15px")


    def next2():
        if (dealer_entry!=""):
                dealer0_entry.insert(0,dealer_entry.get())
        if check_input_values():
            l = []
            l.append(product_entry.get())
            l.append(price_entry.get())
            l.append(dealer0_entry.get())
            l.append(manu_entry.get())
            l.append(exp_entry.get())
            l.append(quantity_entry.get())
            l.append(genre_entry.get())
            print(l)
            global add_stock_details
            add_stock_details.append(l)
            for i in add_stock_details :
                print(i)
            clear()
            

    def save():
        if check_input_values():
            print("save to data base")
            print(add_stock_details)

    def exit1():
        stock.withdraw

    global add_stock_details
    add_stock_details = []

    stock = tk.Toplevel(root)
    stock.geometry("500x800")
    stock.title("adding stock")

    #label
    title_label = tk.Label(stock,text="Adding Stock",fg="purple",font="25px")
    dealer_label = tk.Label(stock,text= "DEALER" ,fg="green")
    product_label = tk.Label(stock,text="product name"  ,fg="green")
    price_label = tk.Label(stock,text="price($)"  ,fg="green")
    dealer0_label = tk.Label(stock,text="dealer"  ,fg="green")
    manu_label = tk.Label(stock,text="manu date"  ,fg="green")
    exp_label = tk.Label(stock,text="exp date"  ,fg="green")
    quantity_label = tk.Label(stock,text="quantity"  ,fg="green")
    total_label = tk.Label(stock,text="total : "  ,fg="green")
    genre_label = tk.Label(stock,text="Genre",fg="blue")
    warnings_label = tk.Label(stock,text="warnings",fg="green")


    #entry fields
    dealer_entry = tk.Entry(stock)
    product_entry = tk.Entry(stock)
    price_entry = tk.Entry(stock)
    dealer0_entry = tk.Entry(stock)
    manu_entry = tk.Entry(stock)
    exp_entry = tk.Entry(stock)
    quantity_entry = tk.Entry(stock)
    genre_entry = tk.Entry(stock)
    def on_enter(event):
        stock.config(bg="black")
    def on_leave(event):
        stock.config(bg="skyblue")

    #hover settings
    dealer_entry.bind("<Enter>",on_enter)
    product_entry.bind("<Enter>",on_enter)
    price_entry.bind("<Enter>",on_enter)
    dealer0_entry.bind("<Enter>",on_enter)
    manu_entry.bind("<Enter>",on_enter)
    exp_entry.bind("<Enter>",on_enter)
    quantity_entry.bind("<Enter>",on_enter)
    genre_entry.bind("<Enter>",on_enter)

    dealer_entry.bind("<Leave>",on_leave)
    price_entry.bind("<Leave>",on_leave)
    product_entry.bind("<Leave>",on_leave)
    dealer0_entry.bind("<Leave>",on_leave)
    manu_entry.bind("<Leave>",on_leave)
    exp_entry.bind("<Leave>",on_leave)
    quantity_entry.bind("<Leave>",on_leave)
    genre_entry.bind("<Leave>",on_leave)



    #buuton fields
    c0 = tk.Button(stock,text="CLEAR",fg="red",command=clear0)
    c1 = tk.Button(stock,text="Clear",fg="red",padx=5,width=5,command=clear1 )
    c2 = tk.Button(stock,text="Clear",fg="red",padx=5,width=5,command=clear2 )
    c3 = tk.Button(stock,text="Clear",fg="red",padx=5,width=5,command=clear3 )
    c4 = tk.Button(stock,text="Clear",fg="red",padx=5,width=5,command=clear4 )
    c5 = tk.Button(stock,text="Clear",fg="red",padx=5,width=5,command=clear5 )
    c6 = tk.Button(stock,text="Clear",fg="red",padx=5,width=5,command=clear6 )
    c7 = tk.Button(stock,text="Clear",fg="red",padx=5,width=5,command=clear7 )
    c = tk.Button(stock,text="Clear",fg="red",padx=5,width=10,command=clear )
    next_button = tk.Button(stock,text="Next",fg="black",background="yellow",padx=5,width=20,height=5,command=next2 )
    save_button = tk.Button(stock,text="Save",fg="black",background="green",padx=5,width=20,height=5,command=save )
    exit_button = tk.Button(stock,text="EXIT",font="15px",fg="red",width=10,command=exit1)

    #grid layout
    #label fields
    title_label.grid(row=0,column=0,columnspan=4)
    dealer_label.grid(row=1,column=0)
    product_label.grid(row=2 ,column=0 )
    price_label.grid(row=3 ,column=0 )
    dealer0_label.grid(row=4 ,column=0 )
    manu_label.grid(row=5 ,column=0 )
    exp_label.grid(row=6 ,column=0 )
    quantity_label.grid(row=7 ,column=0 )
    genre_label.grid(row=8,column=0)
    #entry fields
    dealer_entry.grid(row=1 ,column=1)
    product_entry.grid(row=2 ,column=1)
    price_entry.grid(row=3 ,column=1)
    dealer0_entry.grid(row=4 ,column=1)
    manu_entry.grid(row=5 ,column=1)
    exp_entry.grid(row=6 ,column=1)
    quantity_entry.grid(row=7 ,column=1)
    genre_entry.grid(row=8,column=1)

    #clear button fields
    c0.grid(row=1 ,column=2 )
    c1.grid(row=2 ,column=2 )
    c2.grid(row=3 ,column=2 )
    c3.grid(row=4 ,column=2 )
    c4.grid(row=5 ,column=2 )
    c5.grid(row=6 ,column=2 )
    c6.grid(row=7 ,column=2 )
    c7.grid(row=8 ,column=2 )
    c.grid(row=9 ,column=0,columnspan=2 )

    next_button.grid(row=1,column=3)
    save_button.grid(row=4,column=3)
    total_label.grid(row=10,column=0,columnspan=3)
    warnings_label.grid(row=11,column=0,columnspan=2)
    exit_button.grid(row=10,column=3)

root = tk.Tk()
root.geometry("100x100")
button = tk.Button(root,text="click",command=add_stock)
button.grid(row=0,column=0)
root.mainloop()
