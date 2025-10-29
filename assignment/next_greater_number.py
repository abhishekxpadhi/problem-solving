# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

# Input Format

# Only line is the integer n

# Constraints

# 1 <= n <= 231 - 1

# Output Format

# Return the integer as per above conditions

# Sample Input 0

# 12
# Sample Output 0

# 21
# Sample Input 1

# 44342
# Sample Output 1

# 44423
# Sample Input 2

# 765
# Sample Output 2

# -1


def nge_func(n):
    # Convert number to list of digits
    char_nums = list(str(n))
    size = len(char_nums)

    # Step 1: Find first decreasing digit from right (pivot)
    i = size - 2
    while i >= 0 and char_nums[i] >= char_nums[i + 1]:
        i -= 1

    if i < 0:
        return -1  # digits are in descending order → no next permutation

    # Step 2: Find smallest digit > pivot (search from right)
    j = size - 1
    while char_nums[j] <= char_nums[i]:
        j -= 1

    # Step 3: Swap pivot and that digit
    char_nums[i], char_nums[j] = char_nums[j], char_nums[i]

    # Step 4: Reverse the suffix to get the smallest possible sequence
    char_nums[i + 1:] = reversed(char_nums[i + 1:])

    return int(''.join(char_nums))
