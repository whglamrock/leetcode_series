
class Solution(object):
    def moveZeroes(self, nums):

        if not nums: return nums

        count = 0
        for num in nums:
            if num == 0:
                count += 1

        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1

        for k in xrange(count):
            nums[-1 - k] = 0

        #return nums    # the stupid leetcode asks for returning nothing.



nums = [0, 1, 0, 3, 12]
Sol = Solution()
print Sol.moveZeroes(nums)