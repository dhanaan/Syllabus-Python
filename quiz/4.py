from collections import Counter

def top_two(numbers):
    return sorted([num for num, _ in Counter(sorted(numbers, reverse=True)).most_common(2)], reverse=True) # for some reason the counter needs the list to be sorted at first..

the_numbers = [2, 5, 5, 2, 3, 2, 2, 11, 11, 2, 9, 5, 2]
print(top_two(the_numbers))