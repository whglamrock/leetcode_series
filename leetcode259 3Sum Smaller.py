from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        for i in range(2, len(nums)):
            l, r = 0, i - 1
            while l < r:
                threeSum = nums[l] + nums[r] + nums[i]
                if threeSum >= target:
                    r -= 1
                else:
                    ans += r - l
                    l += 1

        return ans


print(Solution().threeSumSmaller([-2, 0, 1, 3], 2))
