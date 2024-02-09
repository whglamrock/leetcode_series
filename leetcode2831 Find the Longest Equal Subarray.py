from collections import defaultdict
from typing import List

# idea similar to lc424: Longest Repeating Character Replacement
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        maxNumCount = 0
        l = 0
        for r, num in enumerate(nums):
            window[num] += 1
            maxNumCount = max(maxNumCount, window[num])
            if r - l + 1 - maxNumCount > k:
                window[nums[l]] -= 1
                if not window[nums[l]]:
                    del window[nums[l]]
                l += 1

        # notice here it wants the length of subarray AFTER REMOVING the different chars, not the original subarray length
        return maxNumCount
