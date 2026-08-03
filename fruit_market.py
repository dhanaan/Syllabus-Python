import take_input as inp

fruits = {
    'apple': 3.00,
    'banana': 2.50,
    'orange': 4.00,
    'grape': 6.50,
    'mango': 5.00,
    'pineapple': 3.50,
    'watermelon': 1.80,
    'strawberry': 8.00,
    'pear': 3.80,
    'kiwi': 7.20
}


total = 0
def show_menu():
    print('\nFRUIT LIST\n=======')
    for fruit in fruits:
        print(f'{fruit}: {fruits.get(fruit):,.2f}/kg')
    print()


order = True
while order:
    show_menu()
    fruit_curr = inp.take_input("Which fruit would you like to buy? ", choices=list(fruits.keys()),case_sensitive=False)
    fruit_grams = inp.take_input("How much do you want? (in grams): ", allow_type=float)
    price = (fruit_grams / 1000) * fruits[fruit_curr]
    print(f"+{fruit_grams}g of {fruit_curr}, total will +${price:,.2f}")
    total += price
    order = True if inp.take_input("Order more? (y/n): ", choices=['y', 'n'], case_sensitive=False) == 'y' else False

print(f'Your total is ${total:,.2f}')

