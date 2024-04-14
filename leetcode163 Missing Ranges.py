from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        n = len(nums)
        ans = []
        if lower < nums[0]:
            ans.append([lower, nums[0] - 1])
        for i in range(n - 1):
            if nums[i + 1] == nums[i] + 1:
                continue
            ans.append([nums[i] + 1, nums[i + 1] - 1])
        if nums[-1] < upper:
            ans.append([nums[-1] + 1, upper])

        return ans
