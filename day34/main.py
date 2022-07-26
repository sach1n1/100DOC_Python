from question_model import Question
from data import questions
from quiz_brain import QuizBrain
from ui import QuizUI

question_bank = []

for q in range(0, 10):
    question_text = questions["results"][q]["question"]
    question_answer = questions["results"][q]["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)
