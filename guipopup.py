
import tkinter as tk
from tkinter import messagebox

def login():
    user = username.get()
    pwd = password.get()
    if not user or not pwd:
        messagebox.showerror("Error", "Fields cannot be empty")
    elif user == "admin" and pwd == "1234":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Credentials")

root = tk.Tk()
username = tk.Entry(root)
password = tk.Entry(root, show="*")

username.pack()
password.pack()

btn = tk.Button(root, text="Login", command=login)
btn.pack()

root.mainloop()
