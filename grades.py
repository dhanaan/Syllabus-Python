students = [
    {"name": "Adam", "grade": 85},
    {"name": "Bob", "grade": 72},
    {"name": "Cole", "grade": 92},
    {"name": "Dean", "grade": 65},
    {"name": "Eve", "grade": 88},
]

passing_grade = 75

passing_students = [student["name"] for student in students if student["grade"] >= passing_grade]

print("Passing students:")
for i, student in enumerate(passing_students, 1):
    print(f'{i}. {student}')