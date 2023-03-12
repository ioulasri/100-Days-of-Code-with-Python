from tkinter import *
from tkinter import messagebox

import algorithm

BACKGROUND_COLOR = "#A1EDE6"
action = 0
shift = 0
new_text = ""


# ---------------------------- COMMANDS ------------------------------- #
def switch():
    global shift, new_text
    new_text = ""
    if action == 1:
        new_text = algorithm.encrypt(text_la.get("0.0", END).lower(), int(shift))
    elif action == 2:
        new_text = algorithm.decrypt(text_la.get("0.0", END).lower(), int(shift))
    print(text_la)
    text_la.delete(0, END)
    text_la.insert(0, new_text.title())


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Cesar Cipher")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

text_label = Label(text="Enter your text: ", font=("Courier", 16, "bold"), bg=BACKGROUND_COLOR, foreground="Black")
text_label.grid(column=0, row=1)

# Text
text_la = Text(height=10, width=50)
text_la.config(font=("Ariel", 20))
# Puts cursor in textbox.
text_la.focus()
# Adds some text to begin with.
text_la.insert(END, "Enter your text here....")
# Gets current value in textbox at line 1, character 0
text_la.grid(column=0, row=2, columnspan=50)

 
# Radiobutton
def radio_used():
    global action
    action = radio_state.get()


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Encrypt", value=1, variable=radio_state, command=radio_used,
                           bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold"), foreground="Black")
radiobutton2 = Radiobutton(text="Decrypt", value=2, variable=radio_state, command=radio_used,
                           bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold"), foreground="Black")
radiobutton1.grid(column=0, row=16)
radiobutton2.grid(column=0, row=17)

# Button
done = Button(text='Convert', command=switch, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0,
              highlightcolor=BACKGROUND_COLOR, foreground="Black", highlightbackground=BACKGROUND_COLOR)
done.grid(column=5, row=15)

shift_label = Label(text="Choose your shift number:", font=("Courier", 16, "bold"), bg=BACKGROUND_COLOR,
                    foreground="Black")
shift_label.grid(column=0, row=15)


# Spinbox
def spinbox_used():
    global shift
    # gets the current value in spinbox.
    shift = spinbox.get()


spinbox = Spinbox(from_=0, to=20, width=5, command=spinbox_used)
spinbox.grid(column=3, row=15)
window.mainloop()
