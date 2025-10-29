# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Input Format

# First line is the length of the array
# Next line is elements of the array

# Constraints

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

# Output Format

# Return single integer that is how much water stored

# Sample Input 0

# 12
# 0 1 0 2 1 0 1 3 2 1 2 1
# Sample Output 0

# 6
# Sample Input 1

# 3
# 1 10 0
# Sample Output 1

# 0

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rain_water' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY hei as parameter.
#

def rain_water(hei):
    # Write your code here
    n = len(hei)
    if n < 3:
        return 0
    
    max_left = hei[0]
    max_right = hei[n-1]
    
    left = 0
    right = n-1
    water = 0
    while left < right:
        if max_left <= max_right:
            left += 1
            max_left = max(max_left, hei[left])
            water += max(0, max_left-hei[left])
        else:
            right -= 1
            max_right = max(max_right, hei[right])
            water += max(0, max_right-hei[right])
    
    return water

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    hei = list(map(int, input().rstrip().split()))

    result = rain_water(hei)

    fptr.write(str(result) + '\n')

    fptr.close()
