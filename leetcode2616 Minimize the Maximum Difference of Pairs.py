from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        # l, r is the min and max possible pair difference after sorting
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = (l + r) // 2
            numOfPairs = 0
            i = 1
            while i < n:
                if nums[i] - nums[i - 1] <= m:
                    numOfPairs += 1
                    i += 2
                # then we will have to take pair nums[i + 1], nums[i]
                else:
                    i += 1
            # the m (pair difference upper limit) is big enough
            if numOfPairs >= p:
                r = m
            else:
                l = m + 1

        # exit condition is l == r
        return l


print(Solution().minimizeMax(nums=[10, 1, 2, 7, 1, 3], p=2))
print(Solution().minimizeMax(nums=[4, 2, 1, 2], p=1))
