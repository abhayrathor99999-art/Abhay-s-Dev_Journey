# Day 9 — OOP Part 1
Date: 19 March 2026

## What I learned
- A class is a blueprint that bundles data and methods together
- __init__ runs automatically when an object is created
- self refers to the specific object calling the method
- Attributes are what an object HAS (self.name, self.color)
- Methods are what an object CAN DO (describe, greet)

## Key syntax
class Cat:
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def describe(self) -> None:
        print(f"{self.name} is a {self.color} cat")

cat1 = Cat("Whisker", "white")
cat1.describe()

## What confused me
- __init__ — what it does and when it runs
- Why self is used everywhere

## Mistakes made
- Used color instead of self as first parameter
- Forgot to add both name and color to __init__
- Forgot comma between parameters

## Connected to
- Password Manager — load_passwords, save_passwords become methods
- filename and passwords list become attributes