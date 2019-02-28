from tkinter import *
from tkinter import ttk
root = Tk()
#adds the message to text box. Depending on which radio button clicked, changes texts and appends user name to front of msg
def messageappend():
    #username variable
    use = user.get()
    #does nothing if entry box is empty
    if message.get() == "":
        return 1
    else:
        if v.get() == 1:
            msg = use + ":" + (message.get()).upper() + "\n"
        elif v.get() == 2:
            msg = use + ":" + (message.get()).lower() + "\n"
        else:
            msg = use + ":" + message.get() + "\n"
    widget6.insert(INSERT, msg)
    #puts focus on entry box
    widget4.focus_set()

#closes window if button pressed
def destruction():
    root.destroy()
#creagtes variables for message and user
message = StringVar()
user = StringVar()

widget1 = ttk.Frame(root, borderwidth=600)

widget6 = Text(root, height=6, state=NORMAL, width=30, padx=1, pady=1)
widget6.grid(row=2, column=1)

widget2 = ttk.Button(root, text="Send", command=messageappend)
widget2.grid(row=3,column=2)

widget4 = ttk.Entry(root, textvariable=message)
widget4.grid(row=4,column=1)

destroy = ttk.Button(root, command=destruction,text="Close")
destroy.grid(row=3,column=3)

ttk.Label(root, text="Username" ).grid(row=3,column=1,sticky=W)

userEntry = ttk.Entry(root, textvariable=user)
userEntry.grid(row=3,column=1,sticky=E)
#Radiobuttons with v as variable holding value
v = IntVar()
Radiobutton(root, text="UPPER", variable=v, value=1,takefocus=False).grid(row=0,column=3)
Radiobutton(root, text="lower", variable=v, value=2, takefocus=False).grid(row=1,column=3)
Radiobutton(root, text="Normal", variable=v, value=3, takefocus=False).grid(row=2,column=3)

#beggining of check boxes
checked1 = BooleanVar()
checked2 = BooleanVar()
checked3 = BooleanVar()
bold = Checkbutton(root, text="Bold", variable=checked1)
bold.grid(row=0,column=4)
italic = Checkbutton(root, text="Italic",variable=checked2)
italic.grid(row=1,column=4)
underlined = Checkbutton(root, text="Underlined",variable=checked3)
underlined.grid(row=2,column=4)
root.mainloop()
