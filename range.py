def is_in_range(num: int):
    if not num >= 1:
        return 'the number must be greater of equal to one!'

    if not num <= 100:
        return 'the number must be smaller or equal to a hundred!'

    return f'{num} is in range of 1 to 100, good'

usr_input = input('choose a number from range 1 to 100: ')
try:
    usr_input = int(usr_input)
    print(is_in_range(usr_input))
except:
    print('that is NOT an integer')
