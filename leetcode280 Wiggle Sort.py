
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        i = 0
        while i < len(nums) - 1:
            if i % 2 == 0:
                if nums[i] > nums[i + 1]:
                    self.exchange(nums, i, i + 1)
            else:
                if nums[i] < nums[i + 1]:
                    self.exchange(nums, i, i + 1)
            i += 1

    def exchange(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp



nums = [2, 9, 8, 7, 2, 1, 5, 6, 4]
Solution().wiggleSort(nums)
print nums



