#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code herei
    arr = []
    for i in range(n):
        arr.append([])

    lastAnswer = 0
    answers = []
    for query in queries:
        t = query[0]
        x = query[1]
        y = query[2]
        if t == 1:
            idx = ((x^lastAnswer)%n)
            arr[idx].append(y)
        elif t == 2:
            idx = ((x^lastAnswer)%n)
            lastAnswer = arr[idx][y%len(arr[idx])]
            answers.append(lastAnswer)
    return answers



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input = '''2 5
    1 0 5
    1 1 7
    1 0 3
    2 1 0
    2 1 1'''

    lines = input.splitlines()
    first_multiple_input = lines[0].rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for line in lines[1:]:
        queries.append(list(map(int, line.rstrip().split())))

    result = dynamicArray(n, queries)

    print(result)                                                    
