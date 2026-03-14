print("=========**Function 1 — `get_passing_students(students)`**==========")
students = [
    ("Abhay",  85, "Chandigarh"),
    ("Rahul",  45, "Delhi"),
    ("Priya",  72, "Chandigarh"),
    ("Amit",   38, "Mumbai"),
    ("Sara",   91, "Delhi"),
    ("Vikram", 67, "Mumbai"),
    ("Neha",   72, "Delhi"),
    ("Rohit",  45, "Chandigarh"),
]

# **Function 1 — `get_passing_students(students)`**
result = [student[0] for student in students if student[1] >= 60]
print(result)

print("=========**Function 2 — `get_unique_cities(students)`**===========")

result = {student[2] for student in students}
print(result )

print("============**Function 3 — `get_score_map(students)`**============")

result = {student[0]: student[1] for student in students}
print(result)

print("=========**Function 4 — `get_sorted_students(students)`**=========")

result = sorted(students, key=lambda student: student[1], reverse=True)
print(result)

print("==========**Function 5 — `get_city_toppers(students)`**===========")

def get_city_toppers(students):
    result = {}
    for name, score, city in students:
        if city not in result:
                result[city]=score
        if result[city] < score:
            result[city]=score
    return result

print(get_city_toppers(students))