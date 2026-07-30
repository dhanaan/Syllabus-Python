import take_input as inp

available_operator = ['+', '-', '*', '/', '**', '//', '%']
operator = inp.take_input(f"Enter an operator {available_operator}: ", choices=available_operator)
num1 = inp.take_input("Enter the 1st number: ", allow_type=float)
num2 = inp.take_input("Enter the 2nd number: ", allow_type=float)

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
elif operator == "**":
    result = num1 ** num2
    print(round(result, 3))
elif operator == "%":
    result = num1 % num2
    print(round(result, 3))
elif operator == "//":
    result = num1 // num2
    print(int(result))


