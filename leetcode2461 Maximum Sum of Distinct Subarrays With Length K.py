from collections import defaultdict
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        l = 0
        ans = 0
        subArray = 0
        for r, num in enumerate(nums):
            window[num] += 1
            subArray += num
            # make sure the window size is k
            while r - l + 1 > k:
                window[nums[l]] -= 1
                subArray -= nums[l]
                if not window[nums[l]]:
                    del window[nums[l]]
                l += 1
            if len(window) == k:
                ans = max(ans, subArray)

        return ans


print(Solution().maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3))
print(Solution().maximumSubarraySum(nums=[4, 4, 4], k=3))
