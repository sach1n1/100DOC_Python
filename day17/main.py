from day17.question_model import QuestionModel
from data import question_data
from day17.quiz_brain import QuizBrain

question_bank = []

for i in range(0, len(question_data)):
    question_bank.append(QuestionModel(question_data[i]["question"], question_data[i]["correct_answer"]))

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"You're final score is {quiz.score}/{quiz.number}")
