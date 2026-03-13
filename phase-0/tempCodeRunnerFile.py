print("get_topper(students)===============================================================")

# students = [
#     {"name": "Abhay",  "score": 85, "city": "Chandigarh"},
#     {"name": "Rahul",  "score": 45, "city": "Delhi"},
#     {"name": "Priya",  "score": 72, "city": "Chandigarh"},
#     {"name": "Amit",   "score": 38, "city": "Mumbai"},
#     {"name": "Sara",   "score": 91, "city": "Delhi"},
#     {"name": "Vikram", "score": 67, "city": "Mumbai"}
# ]

# def get_topper(students):
#     topper = students[0]
#     for student in students:
#         if student["score"] > topper["score"]:
#             topper = student
#     return topper 

# print(get_topper(students))


# print("get_average_score(students)=========================================================")

# def get_average_score(students):
#     total = 0.0
#     for student in students:
#         total += student["score"]
#     return total/len(students)

# print(get_average_score(students))


# print("get_passing_students(students)======================================================")

# def get_passing_students(students):
#     best_scorers = []
#     for student in students:
#         if student["score"] >= 60 :
#             best_scorers.append(student)
#     return best_scorers

# print(get_passing_students(students))


# print("get_students_by_city(students, city)================================================")


# def get_students_by_city(students, city):
#     result = []
#     for student in students:
#         if student["city"] == city:
#             result.append(student)
#     return result
    

# print(get_students_by_city(students, "pune"))


# print("add_student(students, name, score, city)============================================")

# def add_student(students, name, score, city):
#     new_student = {
#         "name": name,
#         "score": score,
#         "city": city }
#     students.append(new_student)

#     return students

# print(add_student(students, "Abhi", 70 , "Chandigarh"))


# students = [
#     {"name": "Abhay", "score": 85, "city": "Chandigarh"}
# ]

# def add_student(students, name, score, city):
#     new_student = {"name": name, "score": score, "city": city}
#     students.append(new_student)
#     return students

# add_student(students, "Rahul", 72, "Delhi")
# print(students) 