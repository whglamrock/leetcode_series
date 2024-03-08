from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        ans = []
        # find the first position
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] != target:
                    return [-1, -1]
                break
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        ans.append(l)

        # find the last position
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        ans.append(l)

        return ans


print(Solution().searchRange([2, 2], 2))
print(Solution().searchRange([], 0))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
