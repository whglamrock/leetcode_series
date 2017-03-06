class Solution(object):
    def missingNumber(self, nums):

        return sum(range(len(nums)+1)) - sum(nums)

    # range(len(nums)+1) generates a list[int] like [0,1,2,3,4...len(nums)]. For example: if nums = [0,1,2,4],
    # len(nums) = 4, the list generated is [0,1,2,3,4].

Sol = Solution()
print Sol.missingNumber([1,2])

