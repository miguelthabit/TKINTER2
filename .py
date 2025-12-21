import tkinter as  tk

def showus():
    v1=entry1.get()
    v2=entry2.get()
    result.config(text="The order is " + "chickennugget :" + v1 + " milkshake :" + v2)

root =tk.Tk()
root.title("Miguel")
root.geometry("605x400")
tk.Label(root,text="chicken nuggets .1").pack()
entry1 =tk.Entry(root)
entry1.pack()
tk.Label(root,text="milkshake .2").pack()
entry2 =tk.Entry(root)
entry2.pack()
tk.Button(root,text="click me here",command=showus).pack()
result =tk.Label(root,text="Your order is here")
result.pack()
root.mainloop()
