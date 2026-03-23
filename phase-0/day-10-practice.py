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

# class Animal:
#     def __init__(self, name: str, color: str, toys: list) -> None:
#         self.name = name
#         self.color = color
#         self.toys = toys

#     def describe(self) -> None:
#         print(f'Hello I am {self.name} and my Color is {self.color}')

# class Cat(Animal):
#     @property
#     def info(self) -> str:
#         return f"Cat: {self.name}, Color: {self.color}"

#     def meow(self) -> None:
#         print(f'{self.name} says meow!')

# cat1 = Cat("Kito", "white")
# print(cat1.info)

# class Cat(Animal):
#     # def describe(self) -> None:
#     #     super().describe()
#     #     print(f"I also purr!")
#     def __repr__(self) -> str:
#         return f"Cat(name='{self.name}', color='{self.color}')"

# Cat1 = Cat("kitto", "white")
# # Cat1.describe() 
# print(repr(Cat1))

# class Cat(Animal):
#     def __init__(self, name: str, color: str, toys: list) -> None:
#         super().__init__(name, color)
#         self.toys = toys

#     def __len__(self) -> int:
#         return len(self.toys)

# cat1 = Cat("Kito", "white", ["ball", "string", "mouse"])
# print(len(cat1))  # prints 3


# class Cat(Animal):
#     def __eq__(self, other) -> bool:
#         return self.name == other.name and self.color == other.color and self.toys == other.toys
    
# Cat1 = Cat("Kito", "white", ["ball"])
# Cat2 = Cat("Kito", "white", ["ball"])
# print(Cat1 == Cat2)

# class Cat(Animal):
#     @classmethod
#     def default(cls) -> "Cat":
#         return cls("Unknown", "Unknown", [])

# cat1 = Cat.default()
# print(cat1.name)

# def timer(func):
#     def wrapper():
#         print("Function starting")
#         func()
#         print("Function done.")
#     return wrapper

# @timer
# def greet():
#     print("Hello!")

# greet()

# def count_up():
#     yield 1
#     yield 2
#     yield 3

# gen = count_up()
# print(next(gen))
# print(next(gen))
# print(next(gen))



class Animal:
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color
        
    def describe(self) -> None:
        print(f"Hello I am {self.name} and my color is {self.color}")

# class Cat(Animal):
#     def meow(self) -> None:
#         super().describe()
#         print(f"{self.name} says meow!")
# class Cat(Animal):
#     def describe(self) -> None:
#         super().describe() # runs Animal's describe first
#         print("I also purr!") # then adds Cat's own line


# cat1 = Cat("Kito", "white")
# cat1.describe() 

# class Cat(Animal):
#     def __str__(self) -> str:
#         return f"{self.name} is a {self.color} cat"
#     def __repr__(self) -> str:
#         return f"Cat(name='{self.name}', color='{self.color}')"

# cat1 = Cat("Kito", "white")
# print(cat1) 
# print(repr(cat1)) 

class Cat(Animal):
    def __init__(self, name: str, color: str, toys: list) -> None:
        super().__init__(name, color) 
        self.toys = toys
    def __len__(self) -> int:
        return len(self.toys)

cat1 = Cat("Kito", "white", ["ball", "string", "mouse"])
print(len(cat1))