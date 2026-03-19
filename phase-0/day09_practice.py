# class Cat:
#     def __init__(self,name: str, color: str) -> None:
#         self.name = name
#         self.color = color

#     def describe(self) -> None:
#         print(f"{self.name} is a {self.color} cat")

# Cat1 = Cat("Whisker", "white")
# Cat2 = Cat("catty", "pink")

# Cat1.describe()
# Cat2.describe()

class PasswordManager:
    def __init__(self, filename: str) -> None:
        self.filename = filename
    
    def greet(self) -> None:
        print(f'Password Manager ready. Using file: {self.filename}')

PasswordManager1 = PasswordManager("Password.json")
PasswordManager1.greet()