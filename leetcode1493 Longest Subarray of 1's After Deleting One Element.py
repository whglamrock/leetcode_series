from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        isOne0Deleted = False
        l = 0
        ans = 0
        for r, num in enumerate(nums):
            if num == 0:
                while isOne0Deleted:
                    if nums[l] == 0:
                        isOne0Deleted = False
                    l += 1
                isOne0Deleted = True
            # you must delete one element so it's not ans = max(r - l + 1, ans)
            ans = max(r - l, ans)

        return ans
