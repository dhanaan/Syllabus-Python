from take_input import take_input

def is_in_range(num: int):
    if not num >= 1:
        return 'the number must be more than one!'

    if not num <= 100:
        return 'the number must be greater than a hundred!'

    return f'{num} is in range 1 to 100, ok have a nice day'

usr_input = take_input('choose a number from range 1 to 100: ', allow_type=int)
print(is_in_range(usr_input))

