from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        # it means if y + x > x + y, then y should be the leading one
        nums.sort(key=cmp_to_key(self.compare))
        while len(nums) > 1 and nums[0] == '0':
            nums.pop(0)

        return ''.join(nums)

    # e.g., [3, 35], [34, 35]. use string concatenation comparison
    def compare(self, a: str, b: str) -> int:
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0


print(Solution().largestNumber(nums=[3, 30, 34, 5, 9]))
