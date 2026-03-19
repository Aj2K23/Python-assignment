
import tkinter as tk

def clear_label():
    label.config(text="")
    clear_btn.config(state="disabled")
    restore_btn.config(state="normal")

def restore_label():
    label.config(text="Python GUI Demo")
    restore_btn.config(state="disabled")
    clear_btn.config(state="normal")

root = tk.Tk()
label = tk.Label(root, text="Python GUI Demo")
label.pack()

clear_btn = tk.Button(root, text="Clear", command=clear_label)
clear_btn.pack()

restore_btn = tk.Button(root, text="Restore", command=restore_label, state="disabled")
restore_btn.pack()

root.mainloop()
