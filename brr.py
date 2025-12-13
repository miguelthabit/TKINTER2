import tkinter as tk
from tkinter import messagebox
def showmessage():
    result = messagebox.askyesno("confirmation","Confirm Yes or No Choose Only one option")
    if result :
        print("Yes picked")
    else :
        print(" No picked")

root = tk.Tk()
tk.Button(root,text= "Click to start",command=showmessage).pack(pady=21)
root.mainloop()