import take_input as inp
import string

char_list = list(" " + string.ascii_letters + string.digits + string.punctuation)

def convert():
    usr = inp.take_input("Do you want to encrypt/decrypt? (e/d): ", choices=['e', 'd'])
    text = inp.take_input("Text: ")

    if usr == 'e':
        for letter in text:
            print (char_list[(char_list.index(letter) + 3) % len(char_list)], end='')
    else:
        for letter in text:
            print (char_list[(char_list.index(letter) - 3) % len(char_list)], end='')

convert()
while inp.take_input("\nagain? (y/n): ", case_sensitive=False, choices=['y', 'n']).lower() == 'y':
    convert()