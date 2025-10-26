# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Input Format

# First line is the length of the array
# Second line is the elements of the array

# Constraints

# 1 <= arr.length <= 3 * 104
# -100 <= arr[i] <= 100
# arr is sorted in non-decreasing order.

# Output Format

# Return length of array after removing duplicates

# Sample Input 0

# 9
# 1 1 1 2 3 4 5 6 7 
# Sample Output 0

# 7

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'remove_dupli' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def remove_dupli(arr):
    # Write your code here
    n = len(arr)
    write = 0
    for read in range(1, n):
        if arr[read] != arr[write]:
            write += 1
            arr[write] = arr[read]
    
    return write+1

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = remove_dupli(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
