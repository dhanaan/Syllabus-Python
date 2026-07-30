from take_input import take_input

name = 'Dhanan'
age = 16
height = 175.1
male = True

print(f'{name} is a {age} years old {"male" if male else "female"} with a height of {height}')
weight = take_input("what about weight? (in kg): ", allow_type=int)
print(f'{name}\'s weight is {weight}kg')