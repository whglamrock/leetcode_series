# O(n) time, O(1) space solution. Note: the output doesn't count as extra space
# If the question asks for not using division, then use the following solution
class Solution(object):
    def productExceptSelf(self, nums):

        n = len(nums)
        res = [0] * len(nums)
        res[0] = 1
        for i in xrange(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        for i in xrange(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


Sol = Solution()
nums = [1,2,3,0]
print Sol.productExceptSelf(nums)
