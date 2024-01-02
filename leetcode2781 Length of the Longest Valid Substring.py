from typing import List

# find the longest valid substring that starts from word[i],
# by scanning the word from right to left.
# The idea is :
# 1) if we find any word[i:k + 1] that are forbidden,
# the search range for the right index immediately decreases to k - 1
# 2) because we are adding chars to the left of the substring one by one,
# if any word[i:k + 1] is forbidden, word[i - 1:k + 1] will be forbidden for sure
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbiddenSet = set(forbidden)
        longest = 0

        r = len(word) - 1
        for l in range(len(word) - 1, -1, -1):
            # max length of forbidden is 10
            for k in range(l, min(l + 10, r + 1)):
                # find the shortest word[l:k + 1] that are in forbidden, then
                # any right bound >= this k will be invalid
                if word[l:k + 1] in forbiddenSet:
                    r = k - 1
                    break
            longest = max(longest, r - l + 1)

        return longest


print(Solution().longestValidSubstring(word="cbaaaabc", forbidden=["aaa", "cb"]))
print(Solution().longestValidSubstring(word="leetcode", forbidden=["de", "le", "e"]))
print(Solution().longestValidSubstring(word="aaaabaaacc", forbidden=["bcca", "aaa", "aabaa", "baaac"]))
