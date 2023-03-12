from tkinter import *
from tkinter import messagebox
import random
import backendGame

BACKGROUND_COLOR = "#A6BEA7"
action = 0
ceil = 0
chances = 10


# ---------------------------- COMMANDS ------------------------------- #
def start():
    global ceil, chances, label_3, random_number
    ceil = entry1.get()
    random_number = random.randint(0, int(ceil))
    print(ceil)
    label_1.config(text=f"Now guess a number between 0 and {ceil}: ")
    radiobutton1.destroy()
    radiobutton2.destroy()
    radiobutton3.destroy()
    label_1.grid(column=0, row=12, columnspan=5)
    label_2.config(text="Enter your guess: ")
    label_2.grid(column=0)
    entry1.grid(column=1)
    if action == 1:
        chances = 12
    elif action == 2:
        chances = 9
    else:
        chances = 5
    label_3 = Label(text=f"You have {chances} chances left !", font=("Courier", 20, "bold"), foreground="Black",
                    bg="#B3AEC3")
    label_3.grid(column=0, row=20)
    button1 = Button(text="Enter", command=guess, width=10, highlightbackground=BACKGROUND_COLOR)
    button1.grid(column=1, row=16)
    button.destroy()
    entry1.delete(0, END)


def guess():
    global chances
    label_2.config(text="Too high! Enter another guess: ")
    label_2.config(text="Too high! Enter another guess: ")
    result = backendGame.guessing(entry1.get(), ceil, random_number)
    if result == 1:
        chances -= 1
        label_2.config(text="Too high! Enter another guess: ")
    elif result == 2:
        chances -= 1
        label_2.config(text="Too low! Enter another guess: ")
    elif result == 3:
        messagebox.showinfo("End", message=f"You won the guess was {random_number}")
        messagebox.askyesno("Evaluation", "Did you like the game ?")
        quit()
    elif result == 4:
        chances -= 1
        messagebox.showerror("Yo", message="Yoo! you went over the ceiling number bruv..")
        label_2.config(text="Enter another guess: ")
    if chances == 0:
        messagebox.showerror("Sorry", message=f"You lost the game, the number was {random_number}")
        quit()
    label_3.config(text=f"You have {chances} chances left !")


# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("Guess the number game")
window.config(padx=15, pady=15, bg="#A6BAB7")

canvas = Canvas(width=800, height=510)
card_front_img = PhotoImage(file="smallerBIGBRAIN.png")
card_background = canvas.create_image(100, 100, image=card_front_img)
card_word = canvas.create_text(400, 90, text="   ARE YOU A BIG BRAIN ??\nWE ARE ABOUT TO FIND OUT..",
                               font=("Couture", 27, "bold"), fill="Black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=8, rowspan=21)

label_3 = Label()
label_1 = Label(text="Choose a difficulty: ", font=("Courier", 20, "bold"), foreground="Black", bg="#B3DEC3")
label_1.grid(row=12, column=0, columnspan=5)


def radio_used():
    global action
    action = radio_state.get()


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="easy", value=1, variable=radio_state, command=radio_used,
                           bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold"), foreground="Black")
radiobutton2 = Radiobutton(text="medium", value=2, variable=radio_state, command=radio_used,
                           bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold"), foreground="Black")
radiobutton3 = Radiobutton(text="hard", value=3, variable=radio_state, command=radio_used,
                           bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold"), foreground="Black")
radiobutton1.grid(column=1, row=13)
radiobutton2.grid(column=2, row=13)
radiobutton3.grid(column=3, row=13)

label_2 = Label(text="Enter a ceiling number to guess to:", font=("Courier", 20, "bold"), foreground="Black",
                bg="#B3DEC3")
label_2.grid(column=1, row=14, columnspan=3)

entry1 = Entry(width=10, bg="Black", background="White", foreground="Black")
entry1.grid(column=3, row=14, columnspan=5)

button = Button(text="START", command=start, width=10, highlightbackground=BACKGROUND_COLOR)
button.grid(column=2, row=16)
random_number = 0

window.mainloop()
