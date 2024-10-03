import tkinter as tk
import mainedit as md

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
                md.main()
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
