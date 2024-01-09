from typing import List

# searching backwards, find the first such nums[i] that nums[i] < nums[i + 1]. mark this i.
# then in nums[i + 1:] find the smallest number that's bigger than nums[i].
# swap them, then sort nums[i + 1:]
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        j = 0
        i = len(nums) - 1
        # find the right most increasing pair
        while i > 0:
            if nums[i] > nums[i - 1]:
                j = i - 1
                break
            i -= 1
        # nums is reversely sorted (e.g., something like [4, 3, 2, 1])
        if i == 0:
            nums.sort()
            return

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[j + 1:] = sorted(nums[j + 1:])
                return


nums1 = [1, 3, 4, 2]
Solution().nextPermutation(nums1)
print(nums1)
nums2 = [1, 1, 5, 1, 1]
Solution().nextPermutation(nums2)
print(nums2)
nums3 = [4, 3, 2, 1]
Solution().nextPermutation(nums3)
print(nums3)
