def take_input(text: str, choices: list = [], allow_type = str,  case_sensitive: bool = True):
    '''just the default input() module but with extended capabilities like: type checking, case sensitive check, choices list'''
    usr_input = input(text)

    if allow_type == str:
        if not choices == []:
            if not case_sensitive:
                usr_input = usr_input.lower()
                choices = [item.lower() for item in choices]
            if usr_input in choices:
                return usr_input
            else:
                print(f'Invalid, please choose between {choices}')
                return take_input(text, choices)
    elif allow_type == int:
        try:
            return int(usr_input)
        except ValueError:
            print(f'Invalid, {usr_input} is not a number')
            return take_input(text, choices, allow_type, case_sensitive)
    elif allow_type == float:
        try:
            return float(usr_input)
        except ValueError:
            print(f'Invalid, {usr_input} is not a number')
            return take_input(text, choices, allow_type, case_sensitive)
    else:
        raise ValueError(f'Unsupported type: {allow_type}')
