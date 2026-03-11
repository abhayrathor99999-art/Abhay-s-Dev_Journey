# ── IF / ELIF / ELSE ────────────────────────────────────────

age = 20

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# ── IMPORTANT: Indentation is not style in Python ──────────
# It is SYNTAX. 4 spaces (or 1 tab) tells Python what belongs
# inside the if block. Wrong indentation = error or wrong behavior.

# ── COMPARISON OPERATORS ───────────────────────────────────
# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to
# ==  equal to
# !=  not equal to

# ── LOGICAL OPERATORS ──────────────────────────────────────
score = 85
attendance = 75

if score >= 80 and attendance >= 75:
    print("Eligible for distinction")

if score >= 80 or attendance >= 75:
    print("Eligible for exam")

if not score < 80:
    print("Score is 80 or above")

# Program 1 — Grade Calculator------------------------------------

score = 70

if score >= 90:
    print("A grade")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
elif score >= 60:
    print("D grade")
else:
    print("Fail")

# Program 2 — Even or Odd------------------------------------------

num = 9

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Program 3 — Login Checker-----------------------------------------

username = "abhay"
password = "123"

userinput_username = input("enter username: ")
userinput_password = input("enter password: ")

if username == userinput_username and password == userinput_password:
    print("Login successful")
elif username == userinput_username and password !=  userinput_password:
    print( "Wrong password")
elif username != userinput_username:
    print("User not found")

# Program 4 — Number Classifier----------------------------------------

num = -9

if num % 2 == 0 and num >= 1:
    print("Positive even")
elif num % 2 != 0 and num >= 1:
    print("Positive odd")
elif num < 0:
    print("Negative number")
elif num == 0:
    print("Zero")

#  FOR LOOP ────────────────────────────────────────────────
# Used when you know how many times to repeat
# range(5) gives: 0, 1, 2, 3, 4

for i in range(5):
    print(f"Number: {i}")

# range(start, stop) — stop is not included
for i in range(1, 6):
    print(f"Count: {i}")    # prints 1 2 3 4 5

# Looping over a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# WHILE LOOP ──────────────────────────────────────────────
# Used when you repeat until a condition becomes False

count = 1
while count <= 5:
    print(f"While count: {count}")
    count += 1      # count = count + 1 — MUST update or infinite loop

# BREAK AND CONTINUE ──────────────────────────────────────

# break  — exit the loop immediately
# continue — skip this iteration, go to next

for i in range(10):
    if i == 5:
        break               # stops at 5
    print(f"Break test: {i}")

for i in range(10):
    if i % 2 == 0:
        continue            # skips even numbers
    print(f"Odd: {i}")

# Program 5 — Multiplication Table------------------------------------

num = 5 

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# Program 6 — Sum of Numbers------------------------------------------

num = 0
for i in range (1, 101):
    num += i
print(f"{num}")

# Program 7 — FizzBuz-------------------------------------------------

for i in range (1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# Program 8 — Number Guessing Game------------------------------------

secret_number = 8
attempts = 0
guess = 0


while True:
    guess = int(input("guess the number: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low, try again")
                
                
    elif guess > secret_number:
        print("too high, try again")  
            
                
    else:  
        print(f"Correct! Secret number was {secret_number}. Total attempts: {attempts}")
        break

        
