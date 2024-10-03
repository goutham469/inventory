import tkinter as tk
import gettingdatafromsql1 as file1

def settings():
    print("inside settings")
    settings_window = tk.Toplevel(root)
    settings_window.geometry("300x400")
    settings_window.config(background="skyblue")

    a=("italic",20)
    b=("italic",30)

    #labels
    main_label = tk.Label(settings_window,text="Settings",font=b)
    data_base_label = tk.Label(settings_window,text="Data Base",font=a)
    file = tk.Label(settings_window,text="files",font=a)

    # buttons
    customers_button = tk.Button(settings_window,text="Cusomers",command=file1.get_customers_data,fg="green",background="orange",height=2)
    purchases_button = tk.Button(settings_window,text="Purchase",command=file1.get_customers_data,fg="green",background="yellow",height=2)
    goods_button = tk.Button(settings_window,text="Goods",command=file1.get_customers_data,fg="green",background="white",height=2)


    main_label.grid(row=0,column=0)
    data_base_label.grid(row=1,column=0,columnspan=2)
    customers_button.grid(row=2,column=0)
    purchases_button.grid(row=2,column=1)
    goods_button.grid(row=2,column=2)
    file.grid(row=3,column=0,columnspan=2)



root  = tk.Tk()

button = tk.Button(root,text="settings",command=settings)

button.grid(row=0,column=0)

root.mainloop()
    