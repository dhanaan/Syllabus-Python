import take_input as inp
import random
import questionsdb
questions = questionsdb.trivia # list of questions ex: ['What is the currency of Japan?', ['Yen', 'Won', 'Dollar', 'Peso']]

def result(asked, correct, answered):
    wrong_list = []
    for i, ans in enumerate(answered):
        if ans != correct[i]:
            wrong_list.append(i)

    print(f"You got {len(answered) - len(wrong_list)}/{len(answered)} question right!")

    if wrong_list != []:
        print("Here's the breakdown of your mistakes: \n")
        for idx in wrong_list:
            print(f'{questions[asked[idx]][0]} ({correct[idx]}) YOU ANSWERED: {answered[idx]}')
    else:
        print('that is Awesome! congrats')

def game_loop(many_question: int = 10):
    asked = []
    correct = []
    answered = []

    rand = random.randint(0, len(questions) - 1)
    print(f"Welcome to quiz, try to answer {many_question} trivia questions")
    question_idx = 1
    while question_idx <= many_question:
        asked.append(rand)
        answer_list = questions[rand][1].copy()
        correct.append(answer_list[0])
        random.shuffle(answer_list)
        print(f'{question_idx}. {questions[rand][0]}')

        for i, ans in enumerate(answer_list):
            print(f'    {"abcd"[i]}. {ans}')

        answer = inp.take_input(": " , choices=['a', 'b', 'c', 'd'], case_sensitive=False)
        answered.append(answer_list["abcd".index(answer)])
        if answered[question_idx - 1] == correct[question_idx - 1]:
            print("-- Correct --")
        else:
            print("-- Wrong --")

        question_idx += 1
        print()

        remaining = [num for num in range(len(questions)) if not num in asked]
        rand = random.choice(remaining)
    result(asked, correct, answered)

def main():
    game_loop(10)
    while inp.take_input("Play again? (y/n): ", choices=['y', 'n'], case_sensitive=False) == 'y':
        print()
        game_loop(10)

    print('Thanks for playing!')

if __name__ == '__main__':
    main()