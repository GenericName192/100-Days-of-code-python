from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_category = question["category"]
    question_bank.append(Question(question_text, question_answer, question_category))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("Well done on finishing the quiz!")
print(f"Your score was {quiz.score} out of {quiz.question_number}")