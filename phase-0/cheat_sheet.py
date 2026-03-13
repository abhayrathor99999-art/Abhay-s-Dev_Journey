# ══════════════════════════════════════════════════════════════════
# PYTHON REFERENCE SHEET — Keep this open while solving exercises
# ══════════════════════════════════════════════════════════════════
# This is NOT for memorizing. It is for LOOKING UP when you forget.
# Professional developers have this open all day. That is normal.
# ══════════════════════════════════════════════════════════════════


# ─────────────────────────────────────────────────────────────────
# 1. VARIABLES AND DATA TYPES
# ─────────────────────────────────────────────────────────────────

name      = "Abhay"       # str   — text, always in quotes
age       = 20            # int   — whole number
height    = 5.9           # float — decimal number
is_student = True         # bool  — only True or False

# Check the type of anything
print(type(name))         # → <class 'str'>

# Convert between types
int("42")                 # → 42       string to int
float("3.14")             # → 3.14     string to float
str(42)                   # → "42"     int to string
bool(0)                   # → False    0 is False, everything else True


# ─────────────────────────────────────────────────────────────────
# 2. OPERATORS
# ─────────────────────────────────────────────────────────────────

# Arithmetic
10 + 3    # → 13   addition
10 - 3    # → 7    subtraction
10 * 3    # → 30   multiplication
10 / 3    # → 3.33 division (always float)
10 // 3   # → 3    floor division (whole number only)
10 % 3    # → 1    modulo (remainder after division)
10 ** 3   # → 1000 power (10 to the power of 3)

# Comparison — always returns True or False
x = 10
x == 10   # → True   equal to
x != 10   # → False  not equal to
x > 5     # → True   greater than
x < 5     # → False  less than
x >= 10   # → True   greater than or equal to
x <= 10   # → True   less than or equal to

# Logical
True and False   # → False  both must be True
True or False    # → True   at least one must be True
not True         # → False  flips True to False

# Shorthand assignment
x += 5    # same as x = x + 5
x -= 5    # same as x = x - 5
x *= 2    # same as x = x * 2
x //= 2   # same as x = x // 2


# ─────────────────────────────────────────────────────────────────
# 3. F-STRINGS — USE ALWAYS FOR STRING FORMATTING
# ─────────────────────────────────────────────────────────────────

name = "Abhay"
age  = 20

print(f"My name is {name}")             # → My name is Abhay
print(f"I am {age} years old")          # → I am 20 years old
print(f"Next year I will be {age + 1}") # → Next year I will be 21
print(f"Type: {type(name)}")            # → Type: <class 'str'>


# ─────────────────────────────────────────────────────────────────
# 4. IF / ELIF / ELSE
# ─────────────────────────────────────────────────────────────────

score = 85

if score >= 90:
    print("A grade")       # runs if score >= 90
elif score >= 80:
    print("B grade")       # runs if score >= 80 AND not already matched
elif score >= 70:
    print("C grade")
else:
    print("Fail")          # runs if nothing above matched

# Ternary — one line if/else
result = "Pass" if score >= 60 else "Fail"


# ─────────────────────────────────────────────────────────────────
# 5. LOOPS
# ─────────────────────────────────────────────────────────────────

# FOR LOOP — when you know how many times
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8  (step of 2)
    print(i)

# Loop over a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# Loop with index using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")   # → 0: apple, 1: banana, 2: mango

# WHILE LOOP — when you don't know how many times
count = 0
while count < 5:
    print(count)
    count += 1    # ALWAYS update or infinite loop

# while True with break — runs until you explicitly stop
while True:
    answer = input("Continue? y/n: ")
    if answer == "n":
        break     # exits the loop

# BREAK AND CONTINUE
for i in range(10):
    if i == 5:
        break      # stop the loop completely at 5
    print(i)       # prints 0,1,2,3,4

for i in range(10):
    if i % 2 == 0:
        continue   # skip this iteration, go to next
    print(i)       # prints 1,3,5,7,9 (odd numbers only)


# ─────────────────────────────────────────────────────────────────
# 6. FUNCTIONS
# ─────────────────────────────────────────────────────────────────

# Define — does nothing until called
def greet(name):           # name is a PARAMETER (placeholder)
    return f"Hello {name}" # return sends value back to caller

# Call — actually runs it
result = greet("Abhay")    # "Abhay" is an ARGUMENT (real value)
print(result)              # → Hello Abhay

# Multiple parameters
def add(a, b):
    return a + b

# Default parameter — used if argument not provided
def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

greet("Abhay")             # → Hello Abhay
greet("Abhay", "Hi")       # → Hi Abhay

# Return multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5])
print(low, high)           # → 1 5


# ─────────────────────────────────────────────────────────────────
# 7. STRINGS — ALL METHODS
# ─────────────────────────────────────────────────────────────────

text = "  Hello, World!  "

# Case
text.upper()               # → "  HELLO, WORLD!  "
text.lower()               # → "  hello, world!  "
text.title()               # → "  Hello, World!  "
text.capitalize()          # → "  hello, world!  " (only first char)
text.swapcase()            # → "  hELLO, wORLD!  "

# Stripping whitespace
text.strip()               # → "Hello, World!"     both sides
text.lstrip()              # → "Hello, World!  "   left only
text.rstrip()              # → "  Hello, World!"   right only

# Searching
"World" in text            # → True
text.find("World")         # → 8   (index) — returns -1 if not found
text.index("World")        # → 8   (index) — CRASHES if not found
text.count("l")            # → 3   how many times l appears
text.startswith("  Hello") # → True
text.endswith("!  ")       # → True

# Replacing and splitting
text.replace("World", "Abhay")  # → "  Hello, Abhay!  "
"a,b,c".split(",")              # → ['a', 'b', 'c']
"a,b,c".split(",", 1)           # → ['a', 'b,c'] (split only once)
" ".join(["Hello", "World"])    # → "Hello World"

# Checking content
"123".isdigit()            # → True  all digits
"abc".isalpha()            # → True  all letters
"abc123".isalnum()         # → True  letters and numbers
"   ".isspace()            # → True  all whitespace
"hello".islower()          # → True  all lowercase
"HELLO".isupper()          # → True  all uppercase

# Length and formatting
len("Hello")               # → 5
"hello".center(11)         # → "   hello   "
"hello".ljust(10)          # → "hello     "
"hello".rjust(10)          # → "     hello"
"hello".zfill(8)           # → "000hello"  (pad with zeros)

# Slicing — works same as lists
text = "Hello"
text[0]                    # → H
text[-1]                   # → o
text[1:3]                  # → el
text[::-1]                 # → olleH  (reversed)


# ─────────────────────────────────────────────────────────────────
# 8. LISTS — ALL METHODS
# ─────────────────────────────────────────────────────────────────

fruits = ["apple", "banana", "mango"]

# ── ADDING ──────────────────────────────────────────────────
fruits.append("orange")         # adds ONE item to END
fruits.insert(1, "grape")       # adds at specific INDEX
fruits.extend(["kiwi", "melon"])# adds ALL items from another list

# ── REMOVING ────────────────────────────────────────────────
fruits.remove("banana")         # removes FIRST occurrence of VALUE
fruits.pop()                    # removes and RETURNS last item
fruits.pop(0)                   # removes and RETURNS item at index 0
fruits.clear()                  # removes ALL items

# ── FINDING ─────────────────────────────────────────────────
fruits = ["apple", "banana", "mango", "banana"]
fruits.index("banana")          # → 1    first occurrence index
fruits.count("banana")          # → 2    how many times it appears
"mango" in fruits               # → True check if exists

# ── ORDERING ────────────────────────────────────────────────
numbers = [3, 1, 4, 1, 5]
numbers.sort()                  # sorts IN PLACE — changes original
numbers.sort(reverse=True)      # sorts descending IN PLACE
sorted(numbers)                 # returns NEW sorted list — original unchanged
numbers.reverse()               # reverses IN PLACE

# ── USEFUL FUNCTIONS ────────────────────────────────────────
len(fruits)                     # number of items
sum([1, 2, 3])                  # → 6    sum of all (numbers only)
min([3, 1, 4])                  # → 1    smallest
max([3, 1, 4])                  # → 4    largest
list(range(1, 6))               # → [1, 2, 3, 4, 5]

# ── SLICING ─────────────────────────────────────────────────
fruits = ["apple", "banana", "mango", "orange", "grape"]
fruits[1:3]                     # → ['banana', 'mango']
fruits[:3]                      # → ['apple', 'banana', 'mango']
fruits[2:]                      # → ['mango', 'orange', 'grape']
fruits[::-1]                    # → reversed list
fruits[::2]                     # → every 2nd item

# ── COPYING ─────────────────────────────────────────────────
copy = fruits.copy()            # shallow copy — use this, not copy = fruits
copy = fruits[:]                # same as above


# ─────────────────────────────────────────────────────────────────
# 9. DICTIONARIES — ALL METHODS
# ─────────────────────────────────────────────────────────────────

student = {"name": "Abhay", "age": 20, "city": "Chandigarh"}

# ── ACCESSING ───────────────────────────────────────────────
student["name"]                     # → Abhay — CRASHES if key missing
student.get("name")                 # → Abhay — safe, returns None if missing
student.get("phone", "not found")   # → "not found" — custom default

# ── ADDING AND UPDATING ─────────────────────────────────────
student["score"] = 90               # add new key
student["age"] = 21                 # update existing key
student.update({"score": 95, "grade": "A"})  # add/update multiple

# ── REMOVING ────────────────────────────────────────────────
student.pop("grade")                # removes key, RETURNS its value
del student["score"]                # removes key, returns nothing
student.popitem()                   # removes and returns LAST inserted pair
student.clear()                     # removes everything

# ── CHECKING ────────────────────────────────────────────────
"name" in student                   # → True   key exists
"phone" not in student              # → True   key does not exist

# ── LOOPING ─────────────────────────────────────────────────
student = {"name": "Abhay", "age": 20, "city": "Chandigarh"}

for key in student:                 # loop through keys
    print(key)

for value in student.values():      # loop through values
    print(value)

for key, value in student.items():  # loop through BOTH — most useful
    print(f"{key}: {value}")

# ── GETTING ALL KEYS/VALUES ─────────────────────────────────
student.keys()                      # all keys
student.values()                    # all values
student.items()                     # all key-value pairs as tuples
len(student)                        # number of keys

# ── COPYING ─────────────────────────────────────────────────
copy = student.copy()               # shallow copy


# ─────────────────────────────────────────────────────────────────
# 10. NESTED DATA — THE TWO MOST COMMON SHAPES
# ─────────────────────────────────────────────────────────────────

# Shape 1 — List of dicts (most common for records)
students = [
    {"name": "Abhay", "age": 20, "score": 85},
    {"name": "Rahul", "age": 21, "score": 92},
    {"name": "Priya", "age": 19, "score": 78}
]
students[0]              # → first student dict
students[0]["name"]      # → "Abhay"
students[1]["score"]     # → 92

for student in students: # loop through all students
    print(student["name"])

# Shape 2 — Dict of lists
classroom = {
    "math":    [85, 92, 78],
    "english": [70, 88, 65]
}
classroom["math"]        # → [85, 92, 78]
classroom["math"][0]     # → 85


# ─────────────────────────────────────────────────────────────────
# 11. THE THREE LOGIC PATTERNS — USE THESE TO SOLVE PROBLEMS
# ─────────────────────────────────────────────────────────────────

# PATTERN 1 — Loop and COLLECT (filter items)
# Use when: you want some items from a list
result = []
for item in items:
    if some_condition(item):
        result.append(item)
# return result

# PATTERN 2 — Loop and ACCUMULATE (build total or dict)
# Use when: you want a running total or count
total = 0
for item in items:
    total += item["value"]
# return total

# PATTERN 3 — Loop and TRACK BEST (find max/min)
# Use when: you want the best/worst item
best = items[0]
for item in items:
    if item["score"] > best["score"]:
        best = item
# return best


# ─────────────────────────────────────────────────────────────────
# 12. INPUT AND OUTPUT
# ─────────────────────────────────────────────────────────────────

name = input("Enter name: ")           # always returns STRING
age  = int(input("Enter age: "))       # convert to int
price = float(input("Enter price: "))  # convert to float

print("Hello")                         # print text
print(f"Hello {name}")                 # print with variable
print("a", "b", "c")                  # → a b c  (space separated)
print("a", "b", "c", sep="-")         # → a-b-c  (custom separator)
print("Hello", end=" ")               # don't add newline at end


# ─────────────────────────────────────────────────────────────────
# 13. LOGIC BUILDING PROCESS — FOLLOW THIS EVERY TIME
# ─────────────────────────────────────────────────────────────────

# STEP 1 — What is the input?
#   One thing → work with it directly
#   Many things → you need a loop

# STEP 2 — What do I need to do?
#   Do it once → just write the code
#   Do it to each item → loop
#   Reuse in multiple places → function

# STEP 3 — What is the output?
#   One value → return it
#   Filtered list → collect pattern
#   Total/count → accumulate pattern
#   Best item → track best pattern

# STEP 4 — Write pseudocode FIRST
#   # get the list of students
#   # start with first student as topper
#   # loop through each student
#   # if this student's score > topper's score → update topper
#   # return topper

# STEP 5 — Code one step at a time
#   Write one line. Test it. Then next line.


# ─────────────────────────────────────────────────────────────────
# QUICK DECISION GUIDE
# ─────────────────────────────────────────────────────────────────
#
# Need to store ONE item with properties? → dict
# Need to store MANY items in order?      → list
# Need to store MANY items with names?    → dict
# Need to check if something exists?      → "x" in collection
# Need to loop through a list?            → for item in list
# Need to loop through a dict?            → for k, v in dict.items()
# Need to filter a list?                  → collect pattern
# Need a total?                           → accumulate pattern
# Need the best item?                     → track best pattern
# Need to reuse logic?                    → function
# Need safe dict access?                  → .get() not []
# Need to add to a list?                  → .append()
# Need to add many to a list?             → .extend()
# Need sorted without changing original? → sorted() not .sort()
#
# ══════════════════════════════════════════════════════════════════