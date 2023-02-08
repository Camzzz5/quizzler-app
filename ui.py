THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        # self.canvas.config(self.canvas)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.text1 = self.canvas.create_text(150,
                                             125,
                                             width=280,
                                             text="question",
                                             fill=THEME_COLOR,
                                             font=("Arial", 20, "italic"))
        self.canvas.itemconfig(self.text1)
        self.label1 = Label(text="Score :0", fg="white", bg=THEME_COLOR)
        self.label1.grid(row=0, column=1)
        self.my_image1 = PhotoImage(file="./images/true.png")
        self.button1 = Button(image=self.my_image1, highlightthickness=0, command=self.true_method)
        self.button1.grid(row=2, column=0)
        self.my_image2 = PhotoImage(file="./images/false.png")
        self.button2 = Button(image=self.my_image2, highlightthickness=0,command=self.false_method)
        self.button2.grid(row=2, column=1,)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.label1.config(text=f"score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text1, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.text1, text="You have reached the end of the game")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def true_method(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_method(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        elif not is_right:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

