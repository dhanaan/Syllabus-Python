def num_to_day(num):
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return day[num - 1] if 0 < num < 8 else "Wrong, please enter a number between 1 and 7"

print(num_to_day(1))
print(num_to_day(0))
print(num_to_day(7))
print(num_to_day(100))