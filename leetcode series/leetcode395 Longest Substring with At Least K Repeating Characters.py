# a great divide and conquer question by baidu...
# O(N^2) solution
class Solution(object):
    def longestSubstring(self, s, k):

        if (not s):
            return 0

        if k == 1:
            return len(s)
        if len(s) < k:
            return 0

        for c in set(s):    # max length of set is 26.
            if s.count(c) < k:  # s.count and s.split both take O(N). Recursion takes O(N). So in total O(N^2)
                return max(self.longestSubstring(substring, k) for substring in s.split(c))

        return len(s)