from take_input import take_input
from random import randint
import questionsdb

questions = questionsdb.trivia
print("Welcome to quiz, win by correctly answering 10 trivia questions")
question_idx = 1
asked = []

while question_idx <= 10:
    rand = randint(0, len(questions) - 1)
    while rand in asked:
        rand = randint(0, len(questions) - 1)
    asked.append(rand)

    curr_question = questions[rand][0]
    answer_list = questions[rand][1]
    print(f'{question_idx}. {curr_question}')
    for i, ans in enumerate(answer_list):
        print(f'    {"abcd"[i]}. {ans}')
    answer = take_input(": " , choices=['a', 'b', 'c', 'd'], case_sensitive=False)
    question_idx += 1
    print()
