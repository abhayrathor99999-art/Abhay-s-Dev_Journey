# List — access by position
person_list = ["Abhay", 20, "Chandigarh"]
print(person_list[0])   # → Abhay — but what is index 0? not obvious

# Dictionary — access by name
person = {
    "name": "Abhay",
    "age": 20,
    "city": "Chandigarh"
}
print(person["name"])   # → Abhay — immediately clear

# Empty dictionary
empty = {}

# Dictionary with data
student = {
    "name": "Abhay",
    "age": 20,
    "city": "Chandigarh",
    "is_student": True,
    "score": 85.5
}

# Keys can be strings or numbers
# Values can be ANY type — string, int, list, another dict, anything

student = {"name": "Abhay", "age": 20, "city": "Chandigarh"}

# Method 1 — square brackets
print(student["name"])    # → Abhay
print(student["age"])     # → 20

# Problem — crashes if key doesn't exist
# print(student["phone"])  # → KeyError: 'phone'

# Method 2 — get() — safe access, no crash
print(student.get("name"))     # → Abhay
print(student.get("phone"))    # → None  (no crash)
print(student.get("phone", "not found"))  # → not found (default value)

student = {"name": "Abhay", "age": 20}

# Adding a new key
student["city"] = "Chandigarh"
print(student)   # → {'name': 'Abhay', 'age': 20, 'city': 'Chandigarh'}

# Updating existing key — same syntax
student["age"] = 21
print(student)   # → {'name': 'Abhay', 'age': 21, 'city': 'Chandigarh'}

# update() — add or update multiple keys at once
student.update({"score": 90, "city": "Delhi"})
print(student)   # → {'name': 'Abhay', 'age': 21, 'city': 'Delhi', 'score': 90}

student = {"name": "Abhay", "age": 20, "city": "Chandigarh", "score": 90}

# pop() — removes key and RETURNS its value
age = student.pop("age")
print(age)       # → 20
print(student)   # → {'name': 'Abhay', 'city': 'Chandigarh', 'score': 90}

# del — removes key, returns nothing
del student["score"]
print(student)   # → {'name': 'Abhay', 'city': 'Chandigarh'}

# clear() — removes everything
student.clear()
print(student)   # → {}

student = {"name": "Abhay", "age": 20}

print("name" in student)     # → True
print("phone" in student)    # → False
print("phone" not in student) # → True

student = {"name": "Abhay", "age": 20, "city": "Chandigarh"}

# Loop through keys only
for key in student:
    print(key)
# → name
# → age
# → city

# Loop through values only
for value in student.values():
    print(value)
# → Abhay
# → 20
# → Chandigarh

# Loop through BOTH key and value — most useful
for key, value in student.items():
    print(f"{key}: {value}")
# → name: Abhay
# → age: 20
# → city: Chandigarh

student = {"name": "Abhay", "age": 20, "city": "Chandigarh"}

# keys() — returns all keys
print(student.keys())     # → dict_keys(['name', 'age', 'city'])

# values() — returns all values
print(student.values())   # → dict_values(['Abhay', 20, 'Chandigarh'])

# items() — returns all key-value pairs as tuples
print(student.items())    # → dict_items([('name', 'Abhay'), ('age', 20), ('city', 'Chandigarh')])

# get() — safe access with optional default
print(student.get("name"))           # → Abhay
print(student.get("phone", "N/A"))   # → N/A

# update() — merge another dict in
student.update({"score": 95, "grade": "A"})
print(student)

# pop() — remove and return
removed = student.pop("grade")
print(removed)    # → A

# popitem() — removes and returns LAST inserted key-value pair
last = student.popitem()
print(last)       # → ('score', 95)

# copy() — makes a shallow copy
copy = student.copy()
print(copy)

# clear() — empties the dict
student.clear()
print(student)    # → {}

students = [
    {"name": "Abhay", "age": 20, "score": 85},
    {"name": "Rahul", "age": 21, "score": 92},
    {"name": "Priya", "age": 19, "score": 78}
]

# Access first student's name
print(students[0]["name"])     # → Abhay

# Access second student's score
print(students[1]["score"])    # → 92

# Loop through all students
for student in students:
    print(f"{student['name']} scored {student['score']}")

# Find highest scorer — using max() with a key
top = max(students, key=lambda s: s["score"])
print(f"Top scorer: {top['name']}")   # → Rahul

# A classroom with subjects and their scores
classroom = {
    "math": [85, 92, 78, 95],
    "english": [70, 88, 65, 90],
    "science": [92, 85, 88, 79]
}

# Access math scores
print(classroom["math"])         # → [85, 92, 78, 95]

# Access first math score
print(classroom["math"][0])      # → 85

# Average math score
avg = sum(classroom["math"]) / len(classroom["math"])
print(f"Math average: {avg}")    # → 87.5