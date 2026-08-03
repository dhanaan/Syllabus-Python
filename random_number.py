import random
import take_input as inp

print("Welcome, guess the lucky number from 1 to 1,000")
random_num = random.randint(1, 1000)
tries = 0
print(random_num)
usr = 0
while usr != random_num:
    tries += 1
    usr = inp.take_input("Guess: ", allow_type=int)
    if usr > random_num:
        print("> Less")
    elif usr < random_num:
        print("> More")

print(f"\nNice you got it in {tries}x try\n")
