
# remember the question asks us to find the "lexicographically smallest" permutation
# idea from: https://discuss.leetcode.com/topic/76208/python-simple-o-n-solution-in-5-lines

class Solution(object):
    def findPermutation(self, s):

        res = []
        for i, char in enumerate(s):
            if char == 'I':
                res.extend(range(i + 1, len(res), -1))

        # try test case like "IDDDD", res should be [1,6,5,4,3,2]
        res.extend(range(len(s) + 1, len(res), - 1))

        return res
