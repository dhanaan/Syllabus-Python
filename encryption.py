import take_input as inp
import string

original = list(" " + string.ascii_letters + string.digits + string.punctuation)

def convert():
    char_list = original.copy()
    usr = inp.take_input("Do you want to encrypt/decrypt? (e/d): ", case_sensitive=False, choices=['e', 'd'])
    text = inp.take_input("Text: ")
    passkey = inp.take_input("Passkey: ")

    # Convert passkey into numbers
    key = [original.index(char) for char in passkey]

    key_idx = 0
    for idx in range(len(char_list)):
        swap = (idx + key[key_idx]) % len(char_list)
        char_list[idx], char_list[swap] = char_list[swap], char_list[idx]
        key_idx = (key_idx + 1) % len(key)

    if usr.lower() == "e":
        encrypted = ""
        for c in text:
            encrypted += char_list[original.index(c)]
        print(encrypted)

    else:
        decrypted = ""
        for c in text:
            decrypted += original[char_list.index(c)]
        print(decrypted)

convert()
while inp.take_input("again? (y/n): ", case_sensitive=False, choices=['y', 'n']).lower() == 'y':
    convert()