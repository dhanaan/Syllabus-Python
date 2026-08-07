def sum_all(*args):
    return sum(args)

def percentage(**kwargs):
    total = sum_all(*kwargs.values()) #unpack the values
    if total > 0:
        print(f'Total: {total}')
        for name, val in kwargs.items():
            print(f'{name}:{val} ({(val/total) * 100:.1f}%)')

percentage(a = 10, b = 21, c = 39, d = 2, e = 16)