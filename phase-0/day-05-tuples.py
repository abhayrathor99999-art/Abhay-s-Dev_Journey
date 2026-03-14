a = (5)
b = (5,)
c = 5,
print(type(a), type(b), type(c))

print("==========================================================")

person = ("Abhay", 20, "Delhi", "Python")
Name, Age, City, language = person

print(f"Name: {Name}\n Age: {Age}\n City: {City}\n Language: {language}")

print("==========================================================")

numbers = (10, 20, 30, 40, 50, 60)
first, *middle, last = numbers 

print(f"First: {first}\nMiddle: {middle}\nLast: {last}")

print("==========================================================")

def circle_stats(radius):
# Unpack the result and print both
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    stats = area, circumference
    return(stats)

area, circumference = circle_stats(5)
print(f"Area: {area}")
print(f"Circumference: {circumference}")

print("==========================================================")

inventory = [
    ("apple", 40, 5),
    ("banana", 20, 12),
    ("mango", 80, 3)
]

total = 0

for fruit, price, units in inventory:
    value = price * units
    total += value
    print(f"{fruit} — ₹{price} x {units} units = ₹{value}")

print(f"Total inventory value: ₹{total}")
