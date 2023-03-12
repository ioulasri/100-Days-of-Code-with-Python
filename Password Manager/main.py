import os
from tkinter import *
from tkinter import messagebox

import PyPassword_generator
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    return PyPassword_generator.generator()


def add():
    a = generate()
    entry3.delete(0, "end")
    entry3.insert(END, string=a)
    pyperclip.copy(a)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=("Courier", 16))
website_label.grid(column=0, row=1)

entry1 = Entry(width=25)
entry1.grid(column=1, row=1)

email_label = Label(text="Email/Username: ", font=("Courier", 16))
email_label.grid(column=0, row=2)

entry2 = Entry(width=35)
entry2.grid(column=1, row=2, columnspan=2)
entry2.insert(END, string="imadoox00@gmail.com")

password_label = Label(text="Password: ", font=("Courier", 16))
password_label.grid(column=0, row=3)

entry3 = Entry(width=25)
entry3.grid(column=1, row=3)
exit_button = Button(window, text="Exit", command=window.quit)
exit_button.grid(column=3, row=4)


def addit():
    new_data = {
        entry1.get().title(): {
            "email": entry2.get(),
            "password": entry3.get(),
        }
    }
    if len(entry1.get()) == 0 or len(entry3.get()) == 0:
        messagebox.showinfo(title="Oops", message="please make sure you don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                messagebox.showinfo(title="Done", message="you successfully added a new password")
                entry1.delete(0, END)
                entry3.delete(0, END)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                messagebox.showinfo(title="Done", message="you successfully added a new password")
        finally:
            entry1.delete(0, END)
            entry3.delete(0, END)


def search():
    try:
        website = entry1.get().title()
        with open("data.json", "r") as f:
            d = json.load(f)
            if website in d:
                email = d[website]["email"]
                password = d[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Oops", message=f"No {website} details were found")
    except:
        messagebox.showinfo(title="Oops", message=f"No data were found")


button1 = Button(text="Generate", command=add)
button1.grid(column=2, row=3)
button2 = Button(text="Add", width=15, command=addit)
button2.grid(column=1, row=4)
button3 = Button(text="Search", width=6, command=search)
button3.grid(column=2, row=1)

window.mainloop()
exit(0)
