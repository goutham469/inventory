import tkinter as tk

def open_child_window():
    child_window = tk.Toplevel(root)
    child_window.title("Child Window")
    
    # Set the size of the child window
    child_window.geometry("300x200")

    # Position the child window relative to the main window
    x = root.winfo_x() + 50  # Adjust the X position as needed
    y = root.winfo_y() + 50  # Adjust the Y position as needed
    child_window.geometry(f"+{x}+{y}")

    # Add widgets and configure the child window as needed
    label = tk.Label(child_window, text="This is a child window")
    label.pack()

root = tk.Tk()
root.title("Main Window")

button = tk.Button(root, text="Open Child Window", command=open_child_window)
button.pack()

root.mainloop()
