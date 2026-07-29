def is_in_range(num: int):
    if not num >= 1:
        return 'the number must be more than one!'

    if not num <= 100:
        return 'the number must be greater than a hundred!'

    return f'{num} is in range 1 to 100, ok have a nice day'

usr_input = input('choose a number from range 1 to 100: ')
try:
    usr_input = int(usr_input)
    print(is_in_range(usr_input))
except:
    print('that is NOT an integer')
