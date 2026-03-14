print("==========================================================")
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1 ^ s2)

print("==========================================================")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
num = set(numbers)
done = sorted(num)

print(done)

print("==========================================================")
student1_correct = {"q1", "q2", "q3", "q5", "q7"}
student2_correct = {"q2", "q3", "q4", "q6", "q7"}

both = student1_correct & student2_correct
only1 = student1_correct - student2_correct
either = student1_correct | student2_correct


print(both)
print(only1)
print(either)