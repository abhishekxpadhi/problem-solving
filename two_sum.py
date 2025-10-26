# Given an array of integers arr and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Input Format

# First line is the length of the array
# Second line is the target value
# Next line contains element of the array

# Constraints

# 2 <= arr.length <= 104
# -109 <= arr[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Output Format

# Return array of indices

# Sample Input 0

# 6
# 3
# 1 2 3 4 5 6
# Sample Output 0

# 0 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'two_sum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER target
#
from collections import defaultdict

def two_sum(arr, target):
    # Write your code here
    mapp = defaultdict(int) # stores key value pair of element and its index
    
    for idx, ele in enumerate(arr):
        if target - ele in mapp:
            return [mapp.get(target-ele), idx]
        mapp[ele] = idx
    
    return []
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    target = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = two_sum(arr, target)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()