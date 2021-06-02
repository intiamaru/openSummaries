#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    maxhg = -float('inf')
    for i in range(1,5):
        for j in range(1,5):
            hg = getHourGlass(arr,i,j)
            if hg >= maxhg: maxhg = hg

    return maxhg

def getHourGlass(arr, i, j):
    result = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
    result += arr[i][j] 
    result += arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
    print(result)    
    return result

if __name__ == '__main__':

    strinput = """-1 -1 0 -9 -2 -2
-2 -1 -6 -8 -2 -5
-1 -1 -1 -2 -3 -4
-1 -9 -2 -4 -4 -5
-7 -3 -3 -2 -9 -9
-1 -3 -1 -2 -4 -5"""

    arr = []

    for i in strinput.splitlines():
        arr.append(list(map(int, i.rstrip().split())))
    result = hourglassSum(arr)

    print(arr)
    print(result)


