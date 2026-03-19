# # INHERITANCE

# class Animal:
#     def __init__(self, name: str, color: str) -> None:
#         self.name = name
#         self.color = color

#     def desCribe(self) -> None:
#         print(f'Hello I am {self.name} and my Color is {self.color}')

# class Cat(Animal):
#     def meow(self) -> None:
#         print(f'{self.name} says meow!')

# Cat1 = Cat("Kito", "white") 
# Cat1.desCribe()
# Cat1.meow()

# # INHERITANCE AND DUNDER - __str__

# class Animal:
#     def __init__(self, name: str, color: str) -> None:
#         self.name = name
#         self.color = color

#     def describe(self) -> None:
#         print(f'Hello I am {self.name} and my Color is {self.color}')

# class Cat(Animal):
#     def __str__(self) -> str:
#         return f"Cat: {self.name}, Color: {self.color}"

#     def meow(self) -> None:
#         print(f'{self.name} says meow!')

# cat1 = Cat("Kito", "white")
# print(cat1)

# INHERITANCE AND DUNDER AND PROPERTY - __str__

class Animal:
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def describe(self) -> None:
        print(f'Hello I am {self.name} and my Color is {self.color}')

class Cat(Animal):
    @property
    def info(self) -> str:
        return f"Cat: {self.name}, Color: {self.color}"

    def meow(self) -> None:
        print(f'{self.name} says meow!')

cat1 = Cat("Kito", "white")
print(cat1.info)