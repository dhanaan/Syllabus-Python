__all__ = ["take_input"]

def _check_type(usr_input, allow_type):
    if allow_type is str:
        return usr_input
    
    try:
        return allow_type(usr_input)
    except ValueError:
        print(f'Invalid, {usr_input} is not a valid {allow_type.__name__}')
        return None

    
def take_input(text: str = "", allow_type = str, case_sensitive: bool = True, choices: list = [], rule = lambda x: True, rule_error: str = "Rule violated"):
    '''input() module with extended capabilities like type checking, case sensitive check, choices list and custom rules'''
    while True:
        usr_input = input(text)
        converted = _check_type(usr_input, allow_type)
            
        if converted is None:
            continue
        try:
            rule_valid = rule(converted)
        except ValueError:
            print(rule_error)
            continue

        if rule_valid:
            if allow_type != str:
                return converted

            # str
            if choices == []:
                return usr_input
            if not case_sensitive:
                usr_input = usr_input.lower()
                choices = [item.lower() for item in choices]
            if usr_input in choices:
                return usr_input
            else:
                print(f'Invalid, please choose between ({", ".join(choices)})')
                continue
        else:
            print(rule_error)
            continue