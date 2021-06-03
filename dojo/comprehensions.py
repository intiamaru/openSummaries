#!/usr/local/bin/python3



# Using lambdas -> filter
def odd(n):
    return filter(lambda x: x%2 == 1, n)

numbers = [0, 1, 2, 3, 4, 5, 6]
print("Lambdas - Selected odd numbers")
print(list(odd(numbers))) # [1, 3, 5]

# Using map
def update(n):
    return map(lambda x: x*2, n)
print("Lambdas - Multiplied by 2")
print(list(update(numbers))) # [0, 2, 4, 6, 8, 10, 12]


import functools as f
# Use sum() for a particular use of reduce()
def sum_of_all_odd(n):
    return f.reduce(lambda x, y: x + y, filter(lambda x: x%2 == 1, n))
    #return sum(x for x in n if x % 2 == 1)
print("Lambdas - Select and sum")
print(sum_of_all_odd(numbers)) # 9


# Use comprehension if clause instead of filter
def odd(n):
    return filter(lambda x: x%2 == 1, n)
    #return (x for x in n if x % 2 == 1)

numbers = [0, 1, 2, 3, 4, 5, 6]
print("Selected odd numbers")
print(list(odd(numbers))) # [1, 3, 5]


# Use comprehension instead of map
def update(n):
    return (x * 2 for x in n)
print("Multiplied by 2")
print(list(update(numbers))) # [0, 2, 4, 6, 8, 10, 12]


# Use sum() for a particular use of reduce()
def sum_of_all_odd(n):
    return sum(x for x in n if x % 2 == 1)
print("Select and sum")
print(sum_of_all_odd(numbers)) # 9
