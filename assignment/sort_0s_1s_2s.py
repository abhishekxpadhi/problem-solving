# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

# Input Format

# Integer N.
# Integer Array of size N.

# Constraints

# 1 <= N <= 10^6
# 0 <= A[i] <= 2
# Output Format

# Integer Array of size N.

# Sample Input 0

# 5
# 0 1 2 1 2
# Sample Output 0

# 0 1 1 2 2
# Explanation 0

# 0s 1s and 2s are segregated into ascending order.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sort_an_array' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def sort_an_array(n, arr):
    # Write your code here
    
    left = 0
    middle = 0
    right = n - 1
   
    while middle <= right:
        if arr[middle] == 1:
            middle+=1
        elif arr[middle] == 0:
            arr[left], arr[middle] = arr[middle], arr[left]
            middle+=1
            left+=1
        else:
            arr[right], arr[middle] = arr[middle], arr[right]
            right-=1
    
    return arr
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = sort_an_array(n, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
