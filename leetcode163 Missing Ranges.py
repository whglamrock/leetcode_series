from collections import deque
from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        nums = deque(nums)
        while nums and nums[0] < lower:
            nums.popleft()
        ans = []
        if nums and nums[0] > lower:
            ans.append([lower, nums[0] - 1])

        # pop out the invalid bigger numbers
        while nums and nums[-1] > upper:
            nums.pop()

        n = len(nums)
        for i in range(n - 1):
            currNum, nextNum = nums[i], nums[i + 1]
            if nextNum - currNum > 1:
                ans.append([currNum + 1, nextNum - 1])

        if nums and nums[-1] < upper:
            ans.append([nums[-1] + 1, upper])

        return ans
