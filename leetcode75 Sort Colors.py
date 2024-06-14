from collections import Counter
from typing import List

# if it needs one pass solution it's much harder. See the 3-way partitioning algo at the bottom
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numCount = Counter(nums)
        i = 0
        for j in range(numCount[0]):
            nums[i] = 0
            i += 1
        for j in range(numCount[1]):
            nums[i] = 1
            i += 1
        for j in range(numCount[2]):
            nums[i] = 2
            i += 1


nums = [0, 1, 2, 2, 1, 0, 2, 1, 1, 2]
Solution().sortColors(nums)
print(nums)


'''
# 3 way partitioning: always swap 0 to left, and swap 2 to right. If it's 1, keep moving rightward
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        
        # P.S.: the condition should i <= r not i < r
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
'''
