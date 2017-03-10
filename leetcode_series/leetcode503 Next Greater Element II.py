
# the idea is still: find consecutively descending subsequence, and the next number will be
#   the "next greater element" of all previous elements in the subsequence

class Solution(object):
    def nextGreaterElements(self, nums):

        if not nums:
            return []

        n = len(nums)
        # stack stores the indices of decreasing elements
        stack = []
        nextgreater = [-1 for i in xrange(n)]

        for i in xrange(2 * n):
            num = nums[i % n]
            while stack and num > nums[stack[-1]]:
                lasti = stack.pop()
                nextgreater[lasti] = num
            if i < n:
                stack.append(i)

        return nextgreater