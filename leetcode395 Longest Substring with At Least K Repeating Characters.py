from collections import defaultdict
from copy import deepcopy
from typing import Dict

# O(N ^ 2) question that should be acceptable in real interview but got TLE in the stupid leetcode
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
                    break
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
# a stupid divide and conquer question initially asked by baidu. In worst case it's still O(N ^ 2) time.
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        if len(s) < k:
            return 0
        
        charCount = Counter(s)
        for char in charCount:
            # we don't need to check any other char whose count < k
            if charCount[char] < k:
                return max(self.longestSubstring(substr, k) for substr in s.split(char))
        
        return len(s)
'''