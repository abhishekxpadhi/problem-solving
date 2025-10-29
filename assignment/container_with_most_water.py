# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Input Format

# First line is the number of vertical lines.
# Secound line is the array having height for each line.

# Constraints

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# Output Format

# Return the maximum amount of water a container can store.

# Sample Input 0

# 2
# 1 1
# Sample Output 0

# 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY height
#

def maxArea(n, height):
    # Write your code here
    left = 0
    right = n-1
    water = 0
    
    while left < right:
        min_height = min(height[right], height[left])
        water = max(water, min_height * (right-left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return water
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    height = list(map(int, input().rstrip().split()))

    result = maxArea(n, height)

    fptr.write(str(result) + '\n')

    fptr.close()
