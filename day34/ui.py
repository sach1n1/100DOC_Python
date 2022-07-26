from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.label = Label(text=f"Score: {self.score}/10", fg="white", bg=THEME_COLOR, font= ("Arial", 14, "italic"))
        self.label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.q_text = self.canvas.create_text(150,
                                              125,
                                              width=280,
                                              text="question",
                                              fill="black",
                                              font=("Arial", 20, "italic"))
        self.get_next_question()
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        tick_img = PhotoImage(file="images/true.png")
        self.tick_btn = Button(image=tick_img, highlightthickness=0, bg=THEME_COLOR,
                               command=lambda: self.check_answer("True"))
        self.tick_btn.grid(row=2, column=0)
        cross_img = PhotoImage(file="images/false.png")
        self.cross_btn = Button(image=cross_img, highlightthickness=0, bg=THEME_COLOR,
                                command=lambda: self.check_answer("False"))
        self.cross_btn.grid(row=2, column=1)
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.q_text, text=q_text)
        if not q_text:
            self.canvas.itemconfig(self.q_text, text="Quiz Complete!")
            messagebox.showinfo(title="Quiz Complete", message=f"Final Score: {self.score}/10")
            self.window.destroy()

    def check_answer(self, user_input):
        self.score, answer = self.quiz.check_answer(user_input)
        self.label.config(text=f"{self.score}/10")
        if answer:
            self.canvas.config(bg='green')
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg='red')
            self.window.after(1000, self.get_next_question)




