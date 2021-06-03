#!/usr/local/bin/python3
list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']

zipped_list = zip(list_a, list_b)

print(list(zipped_list)) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]


zipper_list = [(1, 'a'), (2, 'b'), (3, 'c')]

list_a, list_b = zip(*zipper_list)
print(list_a)# (1, 2, 3)
print(list_b) # ('a', 'b', 'c')
