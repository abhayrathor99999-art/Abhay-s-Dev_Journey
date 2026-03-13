# Day 4 — Lists, Dictionaries, and Logic Patterns

## Concepts learned
- List methods: append, insert, extend, remove, pop, sort, sorted, reverse
- Dict methods: get, update, pop, del, items, keys, values
- Nested data: list of dicts vs dict of lists
- Passing by reference — lists passed to functions share memory

## The Three Patterns
- Pattern 1 Collect: empty list → loop → if condition → append → return
- Pattern 2 Accumulate: total = 0 → loop → total += value → return total
- Pattern 3 Track Best: best = first item → loop → if better → update best → return best

## Logic building process I used today
(after deep learning and understanding things logic building was good)

## What was hard today
before learning in deep and knowing patterns it was hard, mainly without deep learning it was very hard 

## What clicked today
learned in deep helped me

## What I learned about lists and memory (Q5 answer)
Outside:  students ──────────────────┐
                                      ▼
                               [actual list in memory]
                                      ▲
Inside:   students (parameter) ───────┘
In Python, when you pass a list to a function, you're not passing a copy. You're passing a reference — a pointer to the same list in memory. So when you do students.append() inside the function, you're modifying the exact same list that exists outside.

# pattern used 
Pattern A — starts with best = items[0], loops, updates best when something better is found
Pattern B — starts with total = 0, loops, adds to total each iteration
Pattern C — starts with result = [], loops, appends items that match a condition


get_topper → A ✅
get_average_score → B ✅
get_passing_students → C ✅
get_students_by_city → C ✅
count_words_frequency → B ✅ — it's building up counts in a dict, that's accumulating
add_stock → None of these — it's just checking if a key exists and updating a value. No loop, no collecting, no tracking best. Just conditional update.
sell_item → None of these — it's just checking conditions and returning messages. No loop at all.
get_low_stock → C ✅

6 and 7 are a new pattern — conditional update/check. Not every function fits A/B/C. Some functions just check a condition and return a result. That's fine.