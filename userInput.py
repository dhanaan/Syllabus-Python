from math import sqrt
from take_input import take_input

usr_input = take_input('get the square root of: ', allow_type=float)
sqt_answer = sqrt(usr_input)
print(f'the square root of {usr_input} is {sqt_answer}')
print(f'because {sqt_answer} times {sqt_answer} is {sqt_answer * sqt_answer}')