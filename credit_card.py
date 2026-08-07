import take_input as inp
# 4111111111111111

# step 1
usr = inp.take_input("Card number: ")
usr = usr.replace("-", "").replace(" ", "")
usr_real = usr

usr = usr[::-1] #flip it

card_provider = {
    "American Express":[34, 37],
    "Mastercard":range(51, 56),
    "Visa":[4]
}
card_length = {
    "American Express":[15],
    "Mastercard":[16],
    "Visa":[13, 16]
}

# step 2
odd, even = 0, 0
now_odd = True

for i in range(len(usr)):
    if now_odd:
        odd += int(usr[i])
        now_odd = False
    else:
        even_mult = int(usr[i]) * 2
        if even_mult > 9:
            even_mult -= 9
        even += even_mult
        now_odd = True

if (odd + even)  % 10 == 0:
    print("Valid card, " ,end='')
    for key, val in card_provider.items():
        for i in val:
            if usr_real.startswith(str(i)) and len(usr_real) in card_length[key]:
                print(f'The provider most likely is {key}')
                break
            
else:
    print("Invalid card")