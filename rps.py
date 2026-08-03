import random
import take_input as inp

options = ('rock', 'paper', 'sciccors')
wins = {
    "r": "s",
    "p": "r",
    "s": "p"
}

play_again = 'y'
while play_again.lower() == 'y':
    robot = random.choice(options)
    usr = inp.take_input("rock, paper, sciccors (r,p,s): ", case_sensitive=False, rule=lambda x: True if x in options or x in ['r', 'p', 's'] else False, rule_error='pick between rock, paper, sciccors only!')
    if len(usr) > 1:
        usr = usr[0]

    if robot[0] == usr:
        print("Draw!")
    elif wins[usr] == robot[0]:
        print(f"You won! because the computer chooses {robot}")
    else:
        print(f"You lose, the computer chooses {robot}")

    play_again = inp.take_input("\nAgain? (y/n): ", case_sensitive=False, choices=['y', 'n'])

print("see you next time..\n")