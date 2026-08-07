import take_input as inp

def show_balance(balance):
    print(f"Balance: ${balance:,.2f}")

def deposit():
    amount = inp.take_input("Enter an amount to be deposited: $", allow_type=float, rule = lambda x: True if x > 0 else False, rule_error="Amount must be more than 0")
    return amount

def withdraw(balance):
    amount = inp.take_input("Enter an amount to withdraw: $", allow_type=float, rule = lambda x: True if x > 0 else False, rule_error="Amount must be more than 0")

    if amount > balance:
        print("Insufficient funds")
        return 0
    else:
        return amount

def main():
    balance = 0
    running = True

    while running:
        print("[BANK] what do you want to do? ")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(inp.take_input('>>> ', choices=['1', '2', '3', '4']))

        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3:
                balance -= withdraw(balance)
            case 4:
                running = False

if __name__ == '__main__':
    main()