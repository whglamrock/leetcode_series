
# DFS  + backtracking solution

class Solution(object):
    def findSubsequences(self, nums):

        res = set()
        self.helper(res, [], 0, nums)
        ans = []
        for item in res:
            ans.append(list(item))

        return ans

    # depth-first search to generate the sequence
    def helper(self, res, curr, index, nums):

        if len(curr) >= 2:
            # list is not hashable type in Python Set
            res.add(tuple(curr))

        for i in xrange(index, len(nums)):
            if len(curr) == 0 or nums[i] >= curr[-1]:
                # append to curr first to avoid "curr + [nums[i]]" in the following recursion
                curr.append(nums[i])
                self.helper(res, curr, i + 1, nums)
                curr.pop()