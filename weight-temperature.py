def take_input(text: str, choices: list):
    usr_input = input(text)
    if usr_input in choices:
        return usr_input
    else:
        print(f'invalid, please choose between {choices}')
        return take_input(text, choices)


mode = ''
weight_unit = ['g', 'kg', 'mg', 'lb', 'oz', 't']

to_grams = [1, 1000, 0.001, 453.592, 28.3495, 1000000]


temp_unit = ['C', 'F', 'K']
mode = take_input('convert weight/temperature (w/t): ', ['w', 't'])
if mode == 'w':
    unit = take_input(f'unit to convert {weight_unit}: ', weight_unit)
else:
    unit = take_input(f'unit to convert {temp_unit}: ', temp_unit)

amount = float(input('amount to convert: '))

if mode == 'w':
    print(f'{amount} {unit} is also equal to')
    
else:
    pass

