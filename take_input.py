def take_input(text: str = "", rule = lambda x: True, choices: list = [], allow_type = str,  case_sensitive: bool = True, rule_error: str = "Rule violated"):
    '''just the default input() module but with extended capabilities like: type checking, case sensitive check, choices list'''
    usr_input = input(text)
    
    # Convert type first
    if allow_type == str:
        converted = usr_input
    elif allow_type == int:
        try:
            converted = int(usr_input)
        except ValueError:
            print(f'Invalid, {usr_input} is not a number')
            return take_input(text=text, rule=rule, choices=choices, allow_type=allow_type, case_sensitive=case_sensitive, rule_error=rule_error)
    elif allow_type == float:
        try:
            converted = float(usr_input)
        except ValueError:
            print(f'Invalid, {usr_input} is not a number')
            return take_input(text=text, rule=rule, choices=choices, allow_type=allow_type, case_sensitive=case_sensitive, rule_error=rule_error)
    else:
        raise ValueError(f'Unsupported type: {allow_type}')
    
    # Now apply rule to converted value
    try:
        rule(converted)
    except ValueError:
        print(rule_error)
        return take_input(text=text, rule=rule, choices=choices, allow_type=allow_type, case_sensitive=case_sensitive, rule_error=rule_error)

    if rule(converted):
        if allow_type == str:
            if choices == []:
                return usr_input
            
            if not case_sensitive:
                usr_input = usr_input.lower()
                choices = [item.lower() for item in choices]
            if usr_input in choices:
                return usr_input
            else:
                print(f'Invalid, please choose between ({", ".join(choices)})')
                return take_input(text=text, rule=rule, choices=choices, allow_type=allow_type, case_sensitive=case_sensitive, rule_error=rule_error)
        else:
            return converted
    else:
        print(rule_error)
        return take_input(text=text, rule=rule, choices=choices, allow_type=allow_type, case_sensitive=case_sensitive, rule_error=rule_error)
