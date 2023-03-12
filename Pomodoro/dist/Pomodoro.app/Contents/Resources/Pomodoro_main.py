import math
import time
from tkinter import *

import pygame as pygame

pygame.mixer.init()
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFF6EA"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_1 = None
clicked = 0


def raise_above_all(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


def play_sound_final():
    pygame.mixer.music.load("/Users/imadoulasri/PycharmProjects/100day/Pomodoro/Complete.ogg")
    pygame.mixer.music.play()


def play_sound_mid():
    pygame.mixer.music.load("/Users/imadoulasri/PycharmProjects/100day/Pomodoro/complsound.ogg")
    pygame.mixer.music.play()


# ---------------------------- TIMER RESET ------------------------------- #
def reset_count():
    window.after_cancel(str(timer_1))
    minutes = 0
    seconds = 0
    canvas.itemconfig(timer, text=f"0{minutes}:{seconds}0")
    title_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def count_start():
    global reps
    if reps % 2 == 0 and reps < 9:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=RED)
        reps += 1
        if reps != 0:
            play_sound_mid()
        raise_above_all(window)
    elif reps % 2 != 0 and reps < 9:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
        reps += 1
        play_sound_mid()
        raise_above_all(window)
    else:
        play_sound_final()
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break")
        reps = 0
        raise_above_all(window)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global clicked
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif int(seconds) < 10:
        seconds = "0" + str(seconds)
    if minutes < 10:
        minutes = "0" + str(minutes)
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer_1
        timer_1 = window.after(1000, count_down, count - 1)
        clicked += 1
    else:
        count_start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=60, pady=50, bg=YELLOW)
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='/Users/imadoulasri/PycharmProjects/100day/Pomodoro/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text='', fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
start_button = Button(text="Start", highlightbackground=YELLOW, command=count_start)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_count)
reset_button.grid(column=2, row=2)

window.mainloop()
