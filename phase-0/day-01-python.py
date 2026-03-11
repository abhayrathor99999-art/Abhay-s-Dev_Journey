# # ── VARIABLES ──────────────────────────────────────────────
# name = "Abhay"
# age = 19
# height = 5.9
# is_student = True

# # ── TYPES ──────────────────────────────────────────────────
# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_student))

# # ── F-STRINGS ──────────────────────────────────────────────
# print(f"My name is {name} and I am {age} years old")
# print(f"In 5 years I will be {age + 5}")

# # ── = vs == ────────────────────────────────────────────────
# x = 10
# print(x == 10)
# print(x == 99)
# print(x != 99)

# ── =  == ────────────────────────────────────────────────

name = "Abhay"
city = "chandigarh"
age = 20
income = 15000.0
have_laptop = True  

print(f"{name} from {city} is {age} years old. Income: {income}. owns laptop: {have_laptop}")

# ── =  == ────────────────────────────────────────────────

print(type("True"))       # <class 'str'>
print(type(10.0))         # <class 'float'> 
print(f"{10 * 5}")        # 50