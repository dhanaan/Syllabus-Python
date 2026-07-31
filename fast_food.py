from take_input import take_input

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

print('ITEM LIST')
col = 0
for item_list, price_list in zip(items, prices):
    col += 1
    for item, price in zip(item_list, price_list):
        print(f'{item} (${price:.2f})', end=' | ')
    print(f'(COLUMN {col})')
print()

order_col = take_input("Which column would you like to choose? ", allow_type=int, rule= lambda x: True if 0 < x <= len(items) else False, rule_error='Invalid column')
order_row = take_input("Which row would you like to choose? ", allow_type=int, rule= lambda x: True if 0 < x <= len(items[0]) else False, rule_error='Invalid row')
order_amount = take_input("How many do you want? ", allow_type=int)
order_name = items[order_col - 1][order_row - 1]
order_price = prices[order_col - 1][order_row - 1]

print(f"For {order_amount} {order_name}, your total will be ${(order_amount * order_price):,.2f}")