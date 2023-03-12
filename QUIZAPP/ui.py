from tkinter import *
from tkinter import messagebox

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def ko(self):
        pass

    def ok(self):
        pass

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0

        self.scoreboard = Label(text=f'score: {self.score}', fg="black", bg=THEME_COLOR, font=("Arial", 15))
        self.scoreboard.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=270,
            text='SOME QUESTION TEXT',
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false,
                                   borderwidth=0)
        self.false_button.grid(column=1, row=2)
        self.correct_button = Button(image=true_image, highlightthickness=0, command=self.correct,
                                     borderwidth=0)
        self.correct_button.grid(column=0, row=2)
        self.check()

        self.window.mainloop()

    def check(self):
        if self.quiz.question_number < len(self.quiz.question_list):
            self.get_next_question()
        else:
            self.false_button.config(state="disabled")
            self.correct_button.config(state="disabled")
            messagebox.showerror("Finished!!", message=f"The quiz is done\nYou got a "
                                                       f"{self.score}/{self.quiz.question_number}")
            quit()

    def correct(self):
        self.quiz.correct_answer = self.quiz.current_question.answer
        if "true" == self.quiz.correct_answer.lower():
            self.score += 1
            self.canvas.config(bg="green")
            self.window.after(1000, lambda : self.foor())
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, lambda: self.foor())

    def false(self):
        self.quiz.correct_answer = self.quiz.current_question.answer
        if "false" == self.quiz.correct_answer.lower():
            self.score += 1
            self.canvas.config(bg="green")
            self.window.after(1000, lambda : self.foor())
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, lambda: self.foor())

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def foor(self):
        self.scoreboard.config(text=f'score: {self.score}')
        self.check()
