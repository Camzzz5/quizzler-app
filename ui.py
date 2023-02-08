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
        self.button1 = Button(image=self.my_image1, highlightthickness=0)
        self.button1.grid(row=2, column=0)
        self.my_image2 = PhotoImage(file="./images/false.png")
        self.button2 = Button(image=self.my_image2, highlightthickness=0)
        self.button2.grid(row=2, column=1,)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text1, text=q_text)

