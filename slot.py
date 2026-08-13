import random
import take_input as inp
from collections import Counter

def main(starting_balance = 1000):
    symbols = ("🍋","🍉", "🍓" ,"🍏", "🥭", "🫐")
    balance = starting_balance
    print("************************")
    print("Welcome to the Fruit Casino!")
    print(f"Symbols: {" ".join(symbols)}")
    print("************************")
    playing = True
    while playing:
        print(f"Current balance: ${balance}")
        bet = inp.take_input("Place your bet: $", allow_type=int, rule=lambda x: True if x <= balance else False, rule_error="Insufficient Funds")
        spin = [random.randint(0, len(symbols) - 1) for _ in range(3)]
        print(("************************"))
        print(f'{"  |  ".join([symbols[item] for item in spin])}')

        count = len(Counter(spin))
        balance -= bet
        if count == 2:
            print(f"Ok you won your bet back plus ${bet // 3}")
            balance += bet + bet // 3
        elif count == 1:
            print(f"Nicee you won your bet back plus ${bet * 3}")
            balance += bet * 4
        else:
            balance -= bet
            print(f"Aw dang it -${bet * 2}")

        playing = inp.take_input("Play again? (y/n): ", choices=["y","n"])
        playing = True if playing == "y" and (balance > 0) else False
        print()
    end_comments(balance, starting_balance)

def end_comments(balance, start):
    if balance == 0:
        print("You've lost everything")
    elif balance < 0:
        print(f"You've lost everything plus a debt of ${0 - balance}")
    elif balance <= start:
        print(f"Ok, you still have ${balance}")
    elif balance == start:
        print("You won and lose nothing, Perfectly balanced as all things should be")
    else:
        print(f"Nice! you now have ${balance}, ${balance - start} richer than before")

if __name__ == '__main__':
    main()