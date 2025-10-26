# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

# Input Format

# First line is the length of the array
# Next line is the elements of the array

# Constraints

# 1 <= arr.length <= 105
# 0 <= arr[i] <= 105

# Output Format

# Return the single element

# Sample Input 0

# 7
# 3 3 7 7 10 11 11
# Sample Output 0

# 10

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'singlelement' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def singlelement(n, arr):
    # Write your code here
    low = 0
    high = n-1
    
    while low<high:
        mid = (low+high)//2
        if arr[mid] == arr[mid^1]:
            low = mid+1
        else:
            high = mid
    
    return arr[low]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = singlelement(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
