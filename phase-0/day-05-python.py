# day-05-python.py
# Day 5 — Comprehensions, Lambda, Map, Filter

print("=== Exercise 1 — List Comprehension: upper ===")
words = ["hello", "world", "python"]
upper_words = [i.upper() for i in words]
print(upper_words)

print("=== Exercise 2 — List Comprehension: odd numbers ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i for i in numbers if i % 2 != 0]
print(result)

print("=== Exercise 3 — List Comprehension: even squares ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i * i for i in numbers if i % 2 == 0]
print(result)

print("=== Exercise 4 — List Comprehension: passing students ===")
students = [
    {"name": "Abhay",  "score": 85, "city": "Chandigarh"},
    {"name": "Rahul",  "score": 45, "city": "Delhi"},
    {"name": "Priya",  "score": 72, "city": "Chandigarh"},
    {"name": "Amit",   "score": 38, "city": "Mumbai"},
    {"name": "Sara",   "score": 91, "city": "Delhi"},
    {"name": "Vikram", "score": 67, "city": "Mumbai"}
]

def get_passing_students(students):
    best_scorer = [i for i in students if i["score"] >= 60]
    return best_scorer

print(get_passing_students(students))

print("=== Exercise 5 — Dict Comprehension: name:length ===")
students_list = ["Abhay", "Rohan", "Priya", "Amit"]
result = {i: len(i) for i in students_list}
print(result)

print("=== Exercise 6 — Dict Comprehension: name:score with condition ===")
students = [
    {"name": "Abhay",  "score": 85},
    {"name": "Rahul",  "score": 45},
    {"name": "Priya",  "score": 72},
    {"name": "Amit",   "score": 38},
    {"name": "Sara",   "score": 91}
]
result = {student["name"]: student["score"] for student in students if student["score"] >= 60}
print(result)

print("=== Exercise 7 — Set Comprehension: even squares ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = {i * i for i in numbers if i % 2 == 0}
print(result)

print("=== Exercise 8 — Lambda: title case ===")
uppers = lambda name: name.title()
print(uppers("abhay"))

print("=== Exercise 9 — Map: title case ===")
names = ["abhay", "rohan", "priya", "amit"]
result = list(map(lambda i: i.title(), names))
print(result)

print("=== Exercise 10 — Filter: score above 60 ===")
students = [
    {"name": "Abhay",  "score": 85},
    {"name": "Rahul",  "score": 45},
    {"name": "Priya",  "score": 72},
    {"name": "Amit",   "score": 38},
    {"name": "Sara",   "score": 91}
]
result = list(filter(lambda student: student["score"] >= 60, students))
print(result)

print("=== Exercise 11 — Sorted with lambda ===")
students = [
    {"name": "Abhay",  "score": 85},
    {"name": "Rahul",  "score": 45},
    {"name": "Priya",  "score": 72},
    {"name": "Amit",   "score": 38},
    {"name": "Sara",   "score": 91}
]
result = sorted(students, key=lambda student: student["score"])
print(result)
