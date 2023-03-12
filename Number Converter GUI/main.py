from tkinter import *
import algo

BACKGROUND_COLOR = "#B3DEA7"
action = 0
action2 = 0


# ---------------------------- COMMANDS ------------------------------- #
def convert():
    if action == 1:
        if action2 == 2:
            a = algo.decimalToBina(int(entry1.get()))
            entry2.delete(0, "end")
            entry2.insert(END, string=str(a))
        elif action2 == 1:
            entry2.delete(0, END)
            entry2.insert(END, string=str(entry1.get()))
        elif action2 == 3:
            a = algo.decimalToHexa(int(entry1.get()))
            entry2.delete(0, END)
            entry2.insert(END, string=str(a))
    elif action == 2:
        if action2 == 1:
            a = algo.BinaToDecimal(int(entry1.get()))
            entry2.delete(0, "end")
            entry2.insert(END, string=str(a))
        elif action2 == 2:
            entry2.delete(0, END)
            entry2.insert(END, string=str(entry1.get()))
        elif action2 == 3:
            a = algo.BinaToHexa(int(entry1.get()))
            entry2.delete(0, END)
            entry2.insert(END, string=str(a))
    elif action == 3:
        if action2 == 1:
            a = algo.HexaToDecimal(entry1.get())
            entry2.delete(0, END)
            entry2.insert(END, string=str(a))
        elif action2 == 2:
            a = algo.HexaToBina(entry1.get())
            entry2.delete(0, END)
            entry2.insert(END, string=str(a))
        elif action2 == 3:
            entry2.delete(0, END)
            entry2.insert(END, string=str(entry1.get()))


# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("Number converter")
window.config(padx=20, pady=20, bg="#E3DEB7")

canvas = Canvas(width=800, height=510)
card_front_img = PhotoImage(file="PENGIUAN.png")
card_background = canvas.create_image(100, 100, image=card_front_img)
card_word = canvas.create_text(480, 90, text="WELCOME TO YOUR NUMBER CONVERTER",
                               font=("Couture", 27, "bold"), fill="Black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=8, rowspan=21)

label_1 = Label(text="Enter a number to convert:", font=("Courier", 20, "bold"), foreground="Black", bg="#B3DEC3")
label_1.grid(column=0, row=10, columnspan=4)
entry1 = Entry(width=20, bg="Black", background="White", foreground="Black")
entry1.grid(column=3, row=10, columnspan=5)

label_2 = Label(text="What is the type of your number:", font=("Courier", 20, "bold"), foreground="Black", bg="#B3DEC3")
label_2.grid(column=1, row=11, columnspan=3)

label_3 = Label(text="Convert to:", font=("Courier", 20, "bold"), foreground="Black", bg="#B3DEC3")
label_3.grid(column=1, row=13, columnspan=3)


def radio_used2():
    global action2
    action2 = radio_state2.get()


# Variable to hold on to which radio button value is checked.
radio_state2 = IntVar()
radiobutton4 = Radiobutton(text="Decimal", value=1, variable=radio_state2, command=radio_used2,
                           bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold"), foreground="Black")
radiobutton5 = Radiobutton(text="Binary", value=2, variable=radio_state2, command=radio_used2,
                           bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold"), foreground="Black")
radiobutton6 = Radiobutton(text="Hexadecimal", value=3, variable=radio_state2, command=radio_used2,
                           bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold"), foreground="Black")
radiobutton4.grid(column=1, row=14)
radiobutton5.grid(column=2, row=14)
radiobutton6.grid(column=3, row=14)

button = Button(text="Convert", command=convert, width=10, highlightbackground=BACKGROUND_COLOR)
button.grid(column=2, row=15)


def radio_used():
    global action
    action = radio_state.get()


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Decimal", value=1, variable=radio_state, command=radio_used,
                           bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold"), foreground="Black")
radiobutton2 = Radiobutton(text="Binary", value=2, variable=radio_state, command=radio_used,
                           bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold"), foreground="Black")
radiobutton3 = Radiobutton(text="Hexadecimal", value=3, variable=radio_state, command=radio_used,
                           bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold"), foreground="Black")
radiobutton1.grid(column=1, row=12)
radiobutton2.grid(column=2, row=12)
radiobutton3.grid(column=3, row=12)

entry2 = Entry(width=20, bg="Black", background="White", foreground="Black")
entry2.grid(column=3, row=15, columnspan=3)

window.mainloop()
