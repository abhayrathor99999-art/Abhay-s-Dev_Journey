# ============================================================
# DAY 6 — File I/O + Error Handling + CSV + JSON
# ============================================================

# BLOCK 1 — Error Handling
# ============================================================
# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#             return None
#     except TypeError:
#             return None

# print(safe_divide(10, 2))  
# print(safe_divide(10, 0))   
# print(safe_divide(10, "x"))

# BLOCK 1 — File Handling
# ============================================================
# Function 1 — save_to_file(filename, content)
# def save_to_file(filename, content):
#     with open(filename,"a") as f:
#         f.write(content)
#     print("saved")
# print(save_to_file("day-06-python.py", "hshkjshkjsbcuiuicsh"))

# #Function 2 — read_from_file(filename)
# def read_from_file(filename):
#     try:
#         with open(filename, "r") as f:
#             content = f.read()
#         return content 
#     except FileNotFoundError:
#         return "File not found"

# print(read_from_file("day-06-python.py"))
# # Test both functions together
# save_to_file("test.txt", "Hello Abhay\n")
# save_to_file("test.txt", "Day 6 learning\n")
# print(read_from_file("test.txt"))
# print(read_from_file("missing.txt"))


# print("JSON==============================================================")

# import json

# data = {"name": "Abhay", "course": "Python", "day": 6}

# def save_json(filename, data):
#     with open(filename, "w") as f:
#         json.dump(data, f, indent=4)
#     return "saved"

# def load_json(filename):
#     try:    
#         with open(filename, "r") as f:
#             content = json.load(f)
#         return content 
#     except FileNotFoundError:
#         return {}

# save_json("test.json", data)
# print(load_json("test.json"))
# print(load_json("missing.json"))
