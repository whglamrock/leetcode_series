class Solution(object):
    def moveZeroes(self, nums):

        count = 0
        for num in nums:
            if num == 0:
                count += 1
        if count == 0: return

        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            while j < len(nums) and nums[j] == 0:
                j += 1
            if i < len(nums) and j < len(nums):
                nums[i] = nums[j]
                i += 1
                j += 1

        for k in xrange(len(nums) - 1, len(nums) - count - 1, -1):
            nums[k] = 0

        #return nums    # the stupid leetcode asks for returning nothing.

nums = [0, 1, 0, 3, 12]
Sol = Solution()
print Sol.moveZeroes(nums)