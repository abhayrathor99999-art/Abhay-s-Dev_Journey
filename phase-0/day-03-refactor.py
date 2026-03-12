#Function 1 — Grade Calculator-----------------------------------------

def returngrade(score):
    if score >= 90:
        return "A grade"
    elif score >= 80:
        return "B grade"
    elif score >= 70:
        return "C grade"
    elif score >= 60:
        return "D grade"
    else:
        return("Fail")

result = returngrade(85)
print(result)


#Function 2 — Even or Odd---------------------------------------------

def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(even_or_odd(4))
print(even_or_odd(7))

#Function 3 — Login Checker----------------------------------------------

def login_checker(username, password, input_username, input_password):
    if input_username == username and input_password == password:
        return "Login successful"
    elif input_username == username and input_password != password:
        return "Wrong password"
    else:
        return "User not found"

print(login_checker("abhay", "123", "abhay", "123"))
print(login_checker("abhay", "123", "abhay", "999"))
print(login_checker("abhay", "123", "rahul", "123"))

#Function 4 — FizzBuzz-----------------------------------------------------

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return str(n)

for i in range(1, 21):
    print(fizzbuzz(i))