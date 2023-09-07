from ui import QuizUI
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from html import unescape

question_bank = []
for question in question_data:
    question_text = unescape(question["question"])
    question_answer = unescape(question["correct_answer"])
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

front_end = QuizUI(quiz)
