# Creating lists
numbers = [1, 2, 3, 4, 5]
names = ["abhay", "rahul", "priya"]
mixed = [1, "hello", True, 3.14]
empty = []

fruits = ["apple", "banana", "mango", "orange", "grape"]
#index:     0         1         2         3         4
#negative: -5        -4        -3        -2        -1

# Positive index — count from start
print(fruits[0])    # → apple
print(fruits[2])    # → mango
print(fruits[4])    # → grape

# Negative index — count from end
print(fruits[-1])   # → grape  (last item)
print(fruits[-2])   # → orange (second from last)
print(fruits[-5])   # → apple  (same as index 0)

fruits = ["apple", "banana", "mango", "orange", "grape"]

print(fruits[1:3])    # → ['banana', 'mango']  (index 1 and 2, not 3)
print(fruits[0:3])    # → ['apple', 'banana', 'mango']
print(fruits[2:])     # → ['mango', 'orange', 'grape']  (2 to end)
print(fruits[:3])     # → ['apple', 'banana', 'mango']  (start to 3)
print(fruits[:])      # → full copy of list
print(fruits[::1])    # → ['apple', 'mango', 'grape']   (every 2nd item)
print(fruits[::-1])   # → ['grape', 'orange', 'mango', 'banana', 'apple'] (reversed)

fruits = ["apple", "banana", "mango"]

# ── ADDING ITEMS ────────────────────────────────────────────

# append() — adds ONE item to the END
fruits.append("orange")
print(fruits)   # → ['apple', 'banana', 'mango', 'orange']

# insert() — adds item at a SPECIFIC position
fruits.insert(1, "grape")   # insert at index 1
print(fruits)   # → ['apple', 'grape', 'banana', 'mango', 'orange']

# extend() — adds ALL items from another list
more = ["kiwi", "melon"]
fruits.extend(more)
print(fruits)   # → ['apple', 'grape', 'banana', 'mango', 'orange', 'kiwi', 'melon']

# ── REMOVING ITEMS ──────────────────────────────────────────

fruits = ["apple", "banana", "mango", "banana"]

# remove() — removes FIRST occurrence of a value
fruits.remove("banana")
print(fruits)   # → ['apple', 'mango', 'banana']  (first banana removed)

# pop() — removes item at index, RETURNS it
# if no index given, removes and returns LAST item
last = fruits.pop()
print(last)     # → banana
print(fruits)   # → ['apple', 'mango']

item = fruits.pop(0)
print(item)     # → apple
print(fruits)   # → ['mango']

# clear() — removes ALL items
fruits.clear()
print(fruits)   # → []

# ── FINDING ITEMS ───────────────────────────────────────────

fruits = ["apple", "banana", "mango", "banana"]

# index() — returns position of first occurrence
print(fruits.index("banana"))   # → 1
print(fruits.index("mango"))    # → 2

# count() — counts how many times value appears
print(fruits.count("banana"))   # → 2
print(fruits.count("apple"))    # → 1

# in — checks if item exists, returns bool
print("mango" in fruits)        # → True
print("grape" in fruits)        # → False

# ── ORDERING ────────────────────────────────────────────────

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() — sorts IN PLACE (modifies original list)
numbers.sort()
print(numbers)              # → [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)
print(numbers)              # → [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() — returns NEW sorted list, original unchanged
original = [3, 1, 4, 1, 5]
new_sorted = sorted(original)
print(original)             # → [3, 1, 4, 1, 5]  (unchanged)
print(new_sorted)           # → [1, 1, 3, 4, 5]

# reverse() — reverses IN PLACE
fruits = ["apple", "banana", "mango"]
fruits.reverse()
print(fruits)               # → ['mango', 'banana', 'apple']

# ── USEFUL FUNCTIONS ────────────────────────────────────────

numbers = [3, 1, 4, 1, 5, 9]

print(len(numbers))         # → 6    (number of items)
print(sum(numbers))         # → 23   (sum of all items)
print(min(numbers))         # → 1    (smallest)
print(max(numbers))         # → 9    (largest)

# sort() modifies the ORIGINAL list — no new list created
numbers = [3, 1, 2]
numbers.sort()
print(numbers)   # → [1, 2, 3] — original changed

# sorted() creates a NEW list — original stays the same
numbers = [3, 1, 2]
new = sorted(numbers)
print(numbers)   # → [3, 1, 2] — original unchanged
print(new)       # → [1, 2, 3] — new sorted list

fruits = ["apple", "banana"]

# append() adds ONE item — even if it's a list, adds as single item
fruits.append(["mango", "orange"])
print(fruits)   # → ['apple', 'banana', ['mango', 'orange']]
#                                        ↑ this is ONE item — a nested list

# extend() adds ALL items from iterable
fruits = ["apple", "banana"]
fruits.extend(["mango", "orange"])
print(fruits)   # → ['apple', 'banana', 'mango', 'orange']
#                                        ↑ two separate items added

fruits = ["apple", "banana", "mango", "orange"]
print(fruits[::1])    # → ['apple', 'banana', 'mango', 'orange']
print(fruits[::2])    # → ['apple', 'mango']
print(fruits[::-1])   # → ['orange', 'mango', 'banana', 'apple']
print(fruits[::-2])   # → ['orange', 'banana']  ← backward, every 2nd
print(fruits[1:4:2])

fruits = ["apple", "banana", "mango", "orange", "grape"]

print(fruits[0:5:2])   # start 0, stop 5, step 2 — what do you get?
print(fruits[1:5:2])   # start 1, stop 5, step 2 — what do you get?
print(fruits[0:4:3])   # start 0, stop 4, step 3 — what do you get?