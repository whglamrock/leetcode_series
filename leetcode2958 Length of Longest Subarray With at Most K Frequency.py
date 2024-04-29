from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        l = 0
        ans = 0
        for r, num in enumerate(nums):
            window[num] += 1
            while window[num] > k and l <= r:
                window[nums[l]] -= 1
                if not window[nums[l]]:
                    del window[nums[l]]
                l += 1

            ans = max(ans, r - l + 1)

        return ans
