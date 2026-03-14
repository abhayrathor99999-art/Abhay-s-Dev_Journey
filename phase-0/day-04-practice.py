# students = [
#     {"name": "Abhay", "score": 85},
#     {"name": "Rahul", "score": 45},
#     {"name": "Priya", "score": 72},
#     {"name": "Amit",  "score": 38},
#     {"name": "Sara",  "score": 91}
# ]

# def above_sixty(students):
#     best = []
#     for score in students:
#         if score["score"] > 60:
#             best.append(score["name"])
#     return best

# print(above_sixty(students))


# print("----------------------------------------------------------------------------------")


# students = [
#     {"name": "Abhay", "score": 85},
#     {"name": "Rahul", "score": 45},
#     {"name": "Priya", "score": 72},
#     {"name": "Amit",  "score": 38},
#     {"name": "Sara",  "score": 91}
# ]

# def get_average_score(students):
#     total = 0
#     for student in students:
#         total += student["score"]
#     return total/len(students)

# print(get_average_score(students))



# print("----------------------------------------------------------------------------------")


# students = [
#     {"name": "Abhay", "score": 85},
#     {"name": "Rahul", "score": 45},
#     {"name": "Priya", "score": 72},
#     {"name": "Amit",  "score": 38},
#     {"name": "Sara",  "score": 91}
# ]


# def get_topper(students):
#     best = students[0]
#     for student in students:
#         if student["score"] > best["score"]:
#             best = student
#     return best

# print(get_topper(students))


# print("----------------------------------------------------------------------------------")


# products = [
#     {"name": "phone",    "price": 15000},
#     {"name": "laptop",   "price": 55000},
#     {"name": "cable",    "price": 199},
#     {"name": "charger",  "price": 499},
#     {"name": "earbuds",  "price": 2999}
# ]


# def get_cheapest_product(products):
#     cheapest = products[0]
#     for product in products:
#         if product["price"] < cheapest["price"]:
#             cheapest = product
#     return cheapest

# print(get_cheapest_product(products))
