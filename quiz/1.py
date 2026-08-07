def say_hello(name = ""):
    return f'Hello, {name.capitalize() or "World"}!'

print(say_hello("aliCE"))
print(say_hello("john"))
print(say_hello())