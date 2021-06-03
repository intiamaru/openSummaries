
#Iterating over a dictionary
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print(map(lambda x : x['name'], dict_a)) # Output: ['python', 'java']
print(map(lambda x : x['points']*10,  dict_a)) # Output: [100, 80]
print(map(lambda x : x['name'] == "python", dict_a)) # Output: [True, False]

# Multiple iterables to Map function
list_a = [1, 2, 3]
list_b = [10, 20, 30]

print(map(lambda x, y: x + y, list_a, list_b))
