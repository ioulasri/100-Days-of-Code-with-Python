class QuizBrain():
    def __init__(self, question_list):
        self.questions = question_list
        self.q = 0

    def NextQuestion(self):
        correct = True
        while correct:
            current_question = self.questions[self.q]
            q = input(f"Q{self.q + 1}: {current_question.text} (True / False): ")
            if q == current_question.answer:
                print("That correct!!")
                print(f"Your score is {self.q+1}/{self.q+1}")
            else:
                print(f"That was wrong!!\nThe correct answer was {current_question.answer}")
                print(f"Your score is {self.q + 1}/{self.q + 1}")
                correct = False
            self.q += 1



