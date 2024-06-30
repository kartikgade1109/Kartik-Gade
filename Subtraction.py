from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning
win = Tk()
win.geometry("700x500")

def add():
    aa = a.get()
    ba = b.get()
    sub_val = int(aa) - int(ba)
    showinfo(title="Subtraction",message=+sub_val)

l1 = Label(win, text="Enter the Numbers to Perform Subtraction", justify="center", fg="red2", font=("Time New Roman", 24))
l1.pack()

l2 = Label(win, text="Enter Number A:", font=(20))
l2.place(x=10, y=70)
a = StringVar()
aad = Entry(win, font=(20), textvariable=a)
aad.place(x=10, y=100)

l3 = Label(win, text="Enter Number B:", font=(20))
l3.place(x=10, y=140)
b = StringVar()
bad = Entry(win, font=(20), textvariable=b)
bad.place(x=10, y=170)

bt1 = Button(win, text="Subtraction", font=(20), command=add)
bt1.place(x=10, y=200)

win.mainloop()
