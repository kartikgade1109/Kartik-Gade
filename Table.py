from tkinter import *

win = Tk()
win.geometry("350x500")
win.title("MyTable")
win.config(bg="yellow")
win.iconbitmap(r"E:\Coding\GUI\Project\mult.ico") 
win.resizable(False, False)

def tab():
    a = n.get()
    table_text = ""
    for i in range(10):
        result = a * (i + 1)
        table_text += f"{a} x {i+1} = {result}\n"
    l3.config(text=table_text)

l1 = Label(win, text="Enter the Number to Print Table", font=("Times New Roman",18),bg="yellow")
l1.pack(pady=10)

l2 = Label(win, text="Enter Number:",bg="yellow",font=("Times New Roman",16))
l2.place(x=10, y=60)

n = IntVar()
t1 = Entry(win, font=60, textvariable=n)
t1.place(x=10, y=90,height=30)

bt = Button(win, text="Generate", command=tab,font=("Times New Roman",14))
bt.place(x=10, y=150)

l3 = Label(win, text="",font=("Times New Roman",14),justify="left",bg="yellow")
l3.place(x=10, y=200)

win.mainloop()


#pyinstaller --onfile -i "icon.ico" file.py