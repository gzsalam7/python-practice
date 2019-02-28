from tkinter import *
from tkinter import ttk
root = Tk()
def messageappend():
    msg = message.get() + "\n"
    widget6.insert(INSERT, msg)

message = StringVar()
widget1 = ttk.Frame(root, borderwidth=600)
widget6 = Text(root, height=6, state=NORMAL, width=5, padx=50, pady=1)
widget6.grid(row=1, column=0,sticky=N)
widget2 = ttk.Button(root, text="WHY", command=messageappend)
widget2.grid(row=2,column=1,sticky=E)
widget4 = ttk.Entry(root, textvariable=message)
widget4.grid(row=2,column=0,sticky=W)

root.mainloop()
