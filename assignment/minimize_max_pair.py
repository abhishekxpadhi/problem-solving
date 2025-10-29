# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

# - For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.

# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

# - Each element of nums is in exactly one pair, and - The maximum pair sum is minimized.

# Return the minimized maximum pair sum after optimally pairing up the elements.

# Input Format

# Integer n. Integer array of length n.

# Constraints

# n == nums.length
# 2 <= n <= 105
# n is even.
# 1 <= nums[i] <= 105
# Output Format

# Integer

# Sample Input 0

# 4
# 3 5 2 3
# Sample Output 0

# 7
# Explanation 0

# The elements can be paired up into pairs (3,3) and (5,2). The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minPairSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def minPairSum(n, arr):
    # Write your code here
    arr.sort()
    max_pair_sum = 0
    
    for i in range(n//2):
        pair_sum = arr[i] + arr[n-i-1]
        max_pair_sum = max(pair_sum, max_pair_sum)
    
    return max_pair_sum
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minPairSum(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
