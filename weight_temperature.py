from take_input import take_input

mode = ''
weight_unit = ['g', 'kg', 'mg', 'lb', 'oz', 't']
to_grams = [1, 1000, 0.001, 453.592, 28.3495, 1000000]

temp_unit = ['C', 'F', 'K', 'R']


def convert_temperature(amount: float, unit: str, unit_to: str) -> float:
    '''Convert temperature between celcius, fahrenheit, kelvin and rankine.
    Input must be their first letter uppercase
    '''

    unit = unit.upper()
    unit_to = unit_to.upper()

    # Convert to Celcius first
    if unit == 'C':
        celsius = amount
    elif unit == 'K':
        celsius = amount - 273.15
    elif unit == 'F':
        celsius = (amount - 32) * 5/9
    elif unit == 'R':
        celsius = (amount - 491.67) * 5/9
    
    # Convert from Celsius to target unit
    if unit_to == 'C':
        return celsius
    elif unit_to == 'K':
        return celsius + 273.15
    elif unit_to == 'F':
        return (celsius * 9/5) + 32
    elif unit_to == 'R':
        return (celsius * 9/5) + 491.67

mode = take_input('Convert Weight/Temperature (w/t): ', choices = ['w', 't'], case_sensitive=False)
if mode == 'w':
    unit = take_input(f'Unit to convert {weight_unit}: ', choices = weight_unit, case_sensitive=False)
else:
    unit = take_input(f'Unit to convert {temp_unit}: ', choices = temp_unit, case_sensitive=False)

amount = take_input('Amount to convert: ', allow_type=float)

print('\n-----------------------')

if mode == 'w':
    idx = weight_unit.index(unit)
    grams = amount * to_grams[idx]
    print(f'{amount} {unit} is also equal to')
    for i, curr_unit in enumerate(weight_unit):
        if curr_unit != unit:
            result = grams / to_grams[i]
            print(f'{result} {curr_unit}')
else:
    print(f'{amount} {unit.upper()} is also equal to')
    for i, curr_unit in enumerate(temp_unit):
        if curr_unit != unit:
            result = convert_temperature(amount, unit, curr_unit.upper())
            print(f'{result:,.1f} {curr_unit}')

print('-----------------------\n')