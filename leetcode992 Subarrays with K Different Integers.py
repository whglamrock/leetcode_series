from collections import defaultdict
from typing import List

# find the longest & shortest good subarray that ends with each nums[i]
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l = 0
        window = defaultdict(int)
        indexToMaxSubarrayLeft = {}
        for r, num in enumerate(nums):
            window[num] += 1
            while len(window) > k:
                window[nums[l]] -= 1
                if not window[nums[l]]:
                    del window[nums[l]]
                l += 1
            if len(window) == k:
                indexToMaxSubarrayLeft[r] = l

        l = 0
        window = defaultdict(int)
        ans = 0
        for r, num in enumerate(nums):
            window[num] += 1
            # first, find a valid window
            while len(window) > k:
                window[nums[l]] -= 1
                if not window[nums[l]]:
                    del window[nums[l]]
                l += 1

            if len(window) < k:
                continue
            # then shrink the window as much as possible
            while l < r and window[nums[l]] > 1:
                window[nums[l]] -= 1
                l += 1

            ans += l - indexToMaxSubarrayLeft[r] + 1

        return ans


print(Solution().subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2))
print(Solution().subarraysWithKDistinct(nums=[1, 2, 1, 3, 4], k=3))
