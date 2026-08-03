import take_input as inp
import string

char_list = list(" " + string.ascii_letters + string.digits + string.punctuation)

def caesar_cipher(shift = 3):
    usr = inp.take_input("Do you want to encrypt/decrypt? (e/d): ", choices=['e', 'd'])
    text = inp.take_input("Text: " )

    result = ""
    if usr == 'e':
        for letter in text:
            if letter in char_list:
                result = result + char_list[(char_list.index(letter) + shift) % len(char_list)]
            else:
                result = result + letter
    else:
        for letter in text:
            if letter in char_list:
                result = result + char_list[(char_list.index(letter) - shift) % len(char_list)]
            else:
                result = result + letter

    print(result)

caesar_cipher()
while inp.take_input("again? (y/n): ", choices=['y', 'n']) == 'y':
    caesar_cipher()