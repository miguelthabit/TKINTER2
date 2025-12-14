import tkinter as tk
from tkinter.filedialog import asksaveasfile
def save ():
    files = [
        ("All Files","*.*"),
        ("Python Files","*.py"),
        ("Text Document","*.txt")
    ]
    file =asksaveasfile(filetypes=files,defaultextension=files)


root = tk.Tk()
tk.Button(root,text= "Click here to save",command=save).pack(pady=21)
root.mainloop()