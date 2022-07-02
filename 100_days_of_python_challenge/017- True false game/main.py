from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

"""
#question = Question(i for i in question_data)
print(question_bank)

#for i in range(len(question_data)):
    for key, val in question_data[i].items():
        print("{} : {}".format(key, val))
        
#question_bank = [(key,val) for i in range(len(question_data)) for key, val in question_data[i].items()]
"""

question_bank = []
for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz, YaaaY!\n")
print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_number}")