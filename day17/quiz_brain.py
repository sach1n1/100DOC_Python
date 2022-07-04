class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.number = 0
        self.score = 0

    def next_question(self):
        answer = input(f"Q{self.number+1}. {self.question_list[self.number].question} (True/False):").title()
        self.check_answer(answer)
        self.number += 1

    def still_has_questions(self):
        return self.number < len(self.question_list)

    def check_answer(self, answer):
        if self.question_list[self.number].answer == answer:
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was {self.question_list[self.number].answer}")
        print(f"Score: {self.score}/{self.number + 1}")
        print("\n")