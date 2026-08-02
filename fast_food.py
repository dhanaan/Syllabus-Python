import take_input as inp

items = [
    ["Pizza", "Burger", "Fried Chicken"],
    ["Hot Dog", "Sandwich", "Fries"],
    ["Ice Cream", "Donut", "Cookie"]
]

prices = [
    [12.99, 8.99, 10.99],
    [2.50, 2.50, 1.50],
    [3.99, 2.99, 2.49]
]
result = 0

def show_menu():
    print('\nITEM LIST')
    col = 0
    for item_list, price_list in zip(items, prices):
        col += 1
        for item, price in zip(item_list, price_list):
            print(f'{item} (${price:.2f})', end=' | ')
        print(f'(COLUMN {col})')
    print()


more_order = True
while more_order:
    show_menu()
    order_col = inp.take_input("Which column would you like to choose? ", allow_type=int, rule= lambda x: True if 0 < x <= len(items) else False, rule_error='Invalid column')
    order_row = inp.take_input("Which row would you like to choose? ", allow_type=int, rule= lambda x: True if 0 < x <= len(items[0]) else False, rule_error='Invalid row')
    order_amount = inp.take_input("How many do you want? ", allow_type=int)
    order_name = items[order_col - 1][order_row - 1]
    order_price = prices[order_col - 1][order_row - 1]
    print(f"+{order_amount} {order_name}, total will +${(order_amount * order_price):,.2f}")
    result += order_amount * order_price
    more_order = True if inp.take_input("Order more? (y/n): ", choices=['y', 'n'], case_sensitive=False) == 'y' else False

print(f'Your total is ${result:,.2f}')