# Day 10 — OOP Part 2
Date: 20 March 2026

## What I learned
- Inheritance — child class gets __init__ and methods from parent for free
- __str__ — controls what prints when you print(object)
- @property — turns a method into an attribute, no brackets needed

## Key syntax

# Inheritance
class Animal:
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

class Cat(Animal):
    def __str__(self) -> str:
        return f"Cat: {self.name}, Color: {self.color}"

    @property
    def info(self) -> str:
        return f"{self.name} is {self.color}"

cat1 = Cat("Kito", "white")
print(cat1)       # uses __str__
print(cat1.info)  # uses @property — no brackets

## What confused me
- Dunder methods — what they are and why they exist
- @property — difference between method call and property access

## Mistakes made
- Wrote Cat class twice instead of combining methods in one class
- Used desCribe instead of describe — snake_case rule

## Connected to
- Password Manager — __str__ can show password entry cleanly
- @property can expose computed data without exposing raw attributes