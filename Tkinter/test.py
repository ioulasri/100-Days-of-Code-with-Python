from tkinter import *

window=Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)
label = Label(text="Hey")
label.grid(column=0, row=0)
button = Button()
button.grid(column=0, row=0)
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")
entry.grid(column=4, row=4)


def button_clicked():
    print("I got clicked")
    new_text = entry.get()
    label.config(text=new_text)


window.mainloop()
