from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0] + k

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            # total num of missing numbers in the left are: nums[m] - nums[l] - (r - l)
            if nums[m] - nums[l] - (m - l) >= k:
                r = m - 1
            else:
                k -= nums[m] - nums[l] - (m - l)
                l = m

        # exit condition has to be l == r
        return nums[l] + k


print(Solution().missingElement(nums=[4, 7, 9, 10], k=1))
print(Solution().missingElement(nums=[4, 7, 9, 10], k=3))
print(Solution().missingElement(nums=[1, 2, 4], k=3))
