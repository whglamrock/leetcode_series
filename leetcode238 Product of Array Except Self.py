
# O(n) time, O(1) space solution. Note: the output doesn't count as extra space
# If the question asks for not using division, then use the following solution

class Solution(object):
    def productExceptSelf(self, nums):

        n = len(nums)
        res = [1] * n   # preset res[i] to 1, saving the "res[0] = 1" step

        # in first pass, make each element of res the product of its left elements (excluding self)
        for i in xrange(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        # e.g., the nums = [1, 2, 3, 4], then res = [1, 1, 2, 6]

        right = 1
        # the second scan (also excluding self) has to start from the last element
        for i in xrange(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res



print Solution().productExceptSelf([1, 2, 3, 0])
