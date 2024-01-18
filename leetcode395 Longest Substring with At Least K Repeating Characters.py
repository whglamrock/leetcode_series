from collections import defaultdict
from copy import deepcopy
from typing import Dict

# O(N^2) question that should be acceptable in real interview but got TLE in the stupid leetcode
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        charCount = defaultdict(int)
        indexToCharCount = {}
        for i, char in enumerate(s):
            charCount[char] += 1
            # deepcopy is O(1) because s is all lowercase letters
            indexToCharCount[i] = deepcopy(charCount)

        ans = 0
        for j in range(len(s)):
            currCharCount = indexToCharCount[j]
            # the substring starts from the first char
            if min(currCharCount.values()) >= k:
                ans = max(ans, j + 1)

            for i in range(j):
                prefixCharCount = indexToCharCount[i]
                if self.isSubstrCharCountsMoreThanK(prefixCharCount, currCharCount, k):
                    ans = max(ans, j - i)
        return ans

    # O(1) because s is all lowercase letters
    def isSubstrCharCountsMoreThanK(self, prefixCharCount: Dict[str, int], currCharCount: Dict[str, int], k: int) -> bool:
        for char in currCharCount:
            # means the some char only exists in prefix
            if currCharCount[char] - prefixCharCount[char] == 0:
                continue
            if currCharCount[char] - prefixCharCount[char] < k:
                return False
        return True


'''
# a stupid divide and conquer question initially asked by baidu...
# O(N^2) time
class Solution(object):
    def longestSubstring(self, s, k):
        if k == 1:
            return len(s)
        if len(s) < k:
            return 0

        for c in set(s):    # max length of set is 26.
            if s.count(c) < k:  # s.count and s.split both take O(N). Recursion takes O(N). So in total O(N^2)
                return max(self.longestSubstring(substring, k) for substring in s.split(c))

        return len(s)
'''