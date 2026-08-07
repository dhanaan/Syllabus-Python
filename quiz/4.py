from collections import Counter

def top_two(numbers):
    return [num for num, _ in Counter(sorted(numbers, reverse=True)).most_common(2)]

the_numbers = [2, 5, 5, 11, 11, 2, 9, 3]
print(top_two(the_numbers))