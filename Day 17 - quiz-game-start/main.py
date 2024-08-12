from data import question_data
from question_model import Question
from quiz_brain import Quiz

#create bank of questions
question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have complete the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)} ")
