from take_input import take_input
import time

loop_type = take_input("Do you want countdown with a while/for loop? ", choices=['while', 'for'])
starting_point = take_input("What number do you want to start with? ", allow_type=int, rule=lambda x: True if x >= 3 else False, rule_error="minimum number 3!")
pause = take_input("How long do you want each iteration to be? (in seconds): ", allow_type=float)

# both loop need to be until -1 so that 0 is outputted too
if loop_type == 'for':
    for i in range(starting_point, -1, -1):
        print(i)
        time.sleep(pause)
    
else:
    num = starting_point
    while num > -1:
        print(num)
        time.sleep(pause)
        num -= 1

print('Countdown Complete')