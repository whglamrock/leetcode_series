
# sufficient and necessary condition to prove the theory is right:
#   https://discuss.leetcode.com/topic/68206/easy-python-solution-with-explaination
# 1) if s in (s + s)[1:-1], it means s is repeated;
# 2) if s is repeated, then s in (s + s)[1:-1]

class Solution(object):
    def repeatedSubstringPattern(self, s):

        return s in (s + s)[1:-1]

