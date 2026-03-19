class Cat:
    def __init__(self,name: str, color: str) -> None:
        self.name = name
        self.color = color

    def describe(self) -> None:
        print(f"{self.name} is a {self.color} cat")

Cat1 = Cat("Whisker", "white")
Cat1.describe()