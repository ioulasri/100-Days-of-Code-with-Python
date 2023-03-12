from tkinter import *

# ---------------------------- NUMBERS -------------------------------- #
NUMBER1 = 0
NUMBER2 = 0
DEC = ""


# ---------------------------- COMMANDS ------------------------------- #
def clear():
    entry1.delete(0, "end")


def one():
    entry1.insert(END, string='1')


def two():
    entry1.insert(END, string='2')


def three():
    entry1.insert(END, string='3')


def four():
    entry1.insert(END, string='4')


def five():
    entry1.insert(END, string='5')


def six():
    entry1.insert(END, string='6')


def seven():
    entry1.insert(END, string='7')


def eight():
    entry1.insert(END, string='8')


def nine():
    entry1.insert(END, string='9')


def zero():
    entry1.insert(END, string='0')


def add():
    global NUMBER1, NUMBER2, DEC
    NUMBER1 = 0
    NUMBER2 = 0
    NUMBER1 = entry1.get()
    DEC = "add"
    entry1.delete(0, "end")


def mul():
    global NUMBER1, NUMBER2, DEC
    NUMBER1 = 0
    NUMBER2 = 0
    NUMBER1 = entry1.get()
    DEC = "mul"
    entry1.delete(0, "end")


def div():
    global NUMBER1, NUMBER2, DEC
    NUMBER1 = 0
    NUMBER2 = 0
    NUMBER1 = entry1.get()
    DEC = "div"
    entry1.delete(0, "end")


def sub():
    global NUMBER1, NUMBER2, DEC
    NUMBER1 = 0
    NUMBER2 = 0
    NUMBER1 = entry1.get()
    DEC = "sub"
    entry1.delete(0, "end")


def equals():
    global NUMBER1, NUMBER2, DEC
    NUMBER2 = entry1.get()
    entry1.delete(0, "end")
    if DEC == "add":
        s = float(NUMBER1) + float(NUMBER2)
        entry1.insert(END, string=str(s))
    elif DEC == "sub":
        s = float(NUMBER1) - float(NUMBER2)
        entry1.insert(END, string=str(s))
    elif DEC == "mul":
        s = float(NUMBER1) * float(NUMBER2)
        entry1.insert(END, string=str(s))
    elif DEC == "div":
        s = float(NUMBER1) / float(NUMBER2)
        entry1.insert(END, string=str(s))


def point():
    entry1.insert(END, string=".")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Calculator")
window.config(padx=20, pady=20, bg="Gray")

entry1 = Entry(width=20, bg="White", background="Black")
entry1.grid(column=0, row=0, columnspan=4)

clear = Button(text="clear", command=clear, highlightbackground='White', border=0)
clear.grid(column=4, row=0)

num1 = Button(text="1", command=one, width=2, highlightbackground='Gray')
num1.grid(column=0, row=1)
num2 = Button(text="2", command=two, width=2, highlightbackground='Gray')
num2.grid(column=1, row=1)
num3 = Button(text="3", command=three, width=2, highlightbackground='Gray')
num3.grid(column=2, row=1)
num4 = Button(text="4", command=four, width=2, highlightbackground='Gray')
num4.grid(column=0, row=2)
num5 = Button(text="5", command=five, width=2, highlightbackground='Gray')
num5.grid(column=1, row=2)
num6 = Button(text="6", command=six, width=2, highlightbackground='Gray')
num6.grid(column=2, row=2)
num7 = Button(text="7", command=seven, width=2, highlightbackground='Gray')
num7.grid(column=0, row=3)
num8 = Button(text="8", command=eight, width=2, highlightbackground='Gray')
num8.grid(column=1, row=3)
num9 = Button(text="9", command=nine, width=2, highlightbackground='Gray')
num9.grid(column=2, row=3)
num0 = Button(text="0", command=zero, width=2, highlightbackground='Gray')
num0.grid(column=1, row=4)
add = Button(text="+", command=add, width=2, highlightbackground='Gray')
add.grid(column=4, row=1)
mul = Button(text="*", command=mul, width=2, highlightbackground='Gray')
mul.grid(column=4, row=2)
div = Button(text="/", command=div, width=2, highlightbackground='Gray')
div.grid(column=4, row=3)
sub = Button(text="-", command=sub, width=2, highlightbackground='Gray')
sub.grid(column=4, row=4)
equ = Button(text="=", command=equals, width=2, highlightbackground='Gray')
equ.grid(column=2, row=4)
point = Button(text=".", command=point, width=2, highlightbackground='Gray')
point.grid(column=0, row=4)

window.mainloop()
