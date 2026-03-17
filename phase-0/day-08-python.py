# # # Add correct type hints to all three functions

# def add(a: float , b: float) -> float:
#     return a + b

# def greet(name: str) -> str:
#     return f"Hello, {name}!"

# def print_score(score: float) -> None:
#     print(f"Score: {score}")

# print(add(10.6, 20))
# print(greet("Abhay"))
# print_score(7.5)


students = [
    {"name": "Abhay",  "score": 85},
    {"name": "Rahul",  "score": 45},
    {"name": "Priya",  "score": 72},
]

def get_passing_students(students: list[dict]) -> list[dict]:
    return [s for s in students if s["score"] >= 60]

print(get_passing_students(students))