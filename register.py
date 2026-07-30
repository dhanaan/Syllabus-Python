from take_input import take_input
print('Register User')

username = take_input('Username: ', rule = lambda x: True if 3 <= len(x) <= 20 and x.find(' ') == -1 and x.isalpha() else False, rule_error = '-------------\nUsername must be:\n3-20 characters\nNo spaces\nOnly alphabet\n-------------')
password = take_input('Password: ', rule = lambda x: True if 3 <= len(x) <= 20 and x.find(' ') == -1 and not x == username else False, rule_error = '-------------\nPassword must be:\n3-20 characters\nNo spaces\nDifferent from the username\n-------------')
email = take_input('Email: ',allow_type=str, rule = lambda x: True if x.index('@') != -1 and len(x) > 3 else False, rule_error='not a valid email')
email_name = email[:email.find('@')]
email_provider = email[email.find('@')+1:]
print(email_name)
print(f'Registered with the name of {username}, your password is {password} and your email name is {email_name} from provider {email_provider}')
