# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window + HashMap approach (O(n) time, O(charset) space)
        # Intuition: Maintain a window [start..i] without repeating chars.
        # If duplicate found within window → move start right of its last seen index.
        # Track max window length as we go.
        n, start, max_cnt = len(s), 0, 0
        mapp = defaultdict(int)  # stores last seen index of each char
        
        for i in range(n):
            if s[i] in mapp and mapp[s[i]] >= start:  # duplicate inside window
                start = mapp[s[i]] + 1                # shrink window from left
            mapp[s[i]] = i                            # update last seen index
            max_cnt = max(max_cnt, i - start + 1)     # update longest window
        
        return max_cnt
