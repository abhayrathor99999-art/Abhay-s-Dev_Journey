# # ── DEFINING A FUNCTION ─────────────────────────────────────
# # def keyword tells Python "I'm defining a function"
# # function name follows same rules as variables
# # parentheses hold the inputs (called parameters)
# # colon starts the function body
# # body is indented 4 spaces — same rule as if/for/while

# def greet():
#     print("Hello, Abhay!")

# # ── CALLING A FUNCTION ──────────────────────────────────────
# # defining a function does NOTHING by itself
# # you must CALL it to make it run

# greet()    # → Hello, Abhay!
# greet()    # → Hello, Abhay! (runs again)
# greet()    # → Hello, Abhay! (runs again)

# # ── PARAMETERS — giving input to a function ─────────────────
# # parameters are variables that only exist inside the function

# def greet_person(name):
#     print(f"Hello, {name}!")

# greet_person("Abhay")   # → Hello, Abhay!
# greet_person("Rahul")   # → Hello, Rahul!
# greet_person("Priya")   # → Hello, Priya!

# # ── MULTIPLE PARAMETERS ─────────────────────────────────────

# def add(a, b):
#     print(f"{a} + {b} = {a + b}")

# add(3, 5)    # → 3 + 5 = 8
# add(10, 20)  # → 10 + 20 = 30

# # ── RETURN ──────────────────────────────────────────────────
# # return sends a value BACK to whoever called the function
# # after return, the function stops immediately

# def add_numbers(a, b):
#     result = a + b
#     return result

# # now you can STORE the returned value
# total = add_numbers(3, 5)
# print(total)           # → 8
# print(total * 2)       # → 16 — you can use it like any variable

# # ── PRINT VS RETURN — understand this deeply ────────────────

# def bad_add(a, b):
#     print(a + b)       # just shows it, gives nothing back

# def good_add(a, b):
#     return a + b       # gives the result back

# # try to use bad_add's result
# x = bad_add(3, 5)      # prints 8, but x gets None
# print(x)               # → None — nothing was returned

# # use good_add's result
# y = good_add(3, 5)     # nothing prints, but y gets 8
# print(y)               # → 8

# # ── EARLY RETURN ────────────────────────────────────────────
# # return exits the function immediately
# # anything after return does NOT run

# def check_age(age):
#     if age < 0:
#         return "Invalid age"
#     if age >= 18:
#         return "Adult"
#     return "Minor"

# print(check_age(-1))   # → Invalid age
# print(check_age(20))   # → Adult
# print(check_age(15))   # → Minor

# # ── LOCAL SCOPE ─────────────────────────────────────────────
# # variables created INSIDE a function only exist inside it
# # they disappear when the function finishes

# def my_function():
#     local_var = "I only exist inside"
#     print(local_var)    # works fine

# my_function()
# # print(local_var)    # ← this would CRASH — local_var doesn't exist here

# # ── GLOBAL SCOPE ────────────────────────────────────────────
# # variables created OUTSIDE functions can be READ inside

# name = "Abhay"         # global variable

# def say_name():
#     print(name)        # can READ global variable

# say_name()             # → Abhay

# # ── THE RULE ────────────────────────────────────────────────
# # functions can READ globals but should not MODIFY them
# # instead — pass values IN as parameters, get values OUT via return
# # this makes functions predictable and testable

# def clean_function(name):    # takes input as parameter
#     greeting = f"Hello {name}"
#     return greeting           # returns output

# result = clean_function("Abhay")
# print(result)

# ── STRING METHODS ───────────────────────────────────────────
text = "  Hello, World!  "

# Case methods
print(text.upper())           # → "  HELLO, WORLD!  "
print(text.lower())           # → "  hello, world!  "

# Stripping whitespace — used constantly for user input cleaning
print(text.strip())           # → "Hello, World!" — removes both sides
print(text.lstrip())          # → "Hello, World!  " — left only
print(text.rstrip())          # → "  Hello, World!" — right only

# Checking content
print(text.strip().startswith("Hello"))   # → True
print(text.strip().endswith("!"))         # → True
print("World" in text)                    # → True — 'in' checks membership

# Replacing
print(text.replace("World", "Abhay"))    # → "  Hello, Abhay!  "

# Splitting — turns a string into a list
sentence = "apple,banana,mango"
fruits = sentence.split(",")
print(fruits)                 # → ['apple', 'banana', 'mango']
print(fruits[0])              # → apple

# Joining — opposite of split, turns list into string
words = ["Hello", "my", "name", "is", "Abhay"]
result = " ".join(words)
print(result)                 # → Hello my name is Abhay

# Finding
email = "abhay@gmail.com"
print(email.find("@"))        # → 5 — index where @ appears
print(len(email))             # → 15 — length of string

# Checking type of content
print("123".isdigit())        # → True — all digits
print("abc".isalpha())        # → True — all letters
print("abc123".isalnum())     # → True — letters and numbers