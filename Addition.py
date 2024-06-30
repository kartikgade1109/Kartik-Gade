from tkinter import *

win = Tk()
win.geometry("700x500")
win.resizable(False, False)

def add():
    aa = a.get()
    ba = b.get()
    sum_val = int(aa) + int(ba)
    l4.config(text="Sum: " + str(sum_val))

l1 = Label(win, text="Enter the Numbers to Perform Addition", justify="center", fg="red2", font=("Time New Roman", 24))
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

bt1 = Button(win, text="Addition", font=(20), command=add)
bt1.place(x=10, y=200)

l4 = Label(win, text="Sum:", font=(20))
l4.place(x=10, y=250)

win.mainloop()