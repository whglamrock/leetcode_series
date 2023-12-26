from typing import List


# sliding window solution
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        ans = 0
        while r < len(nums):
            if nums[r] == 1:
                ans = max(ans, r - l + 1)
            else:
                # need to find the left most 0
                if k == 0:
                    while l < r and nums[l] == 1:
                        l += 1
                    # popleft the left most 0
                    l += 1
                else:
                    k -= 1
                ans = max(ans, r - l + 1)
            r += 1

        return ans


print(Solution().longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(Solution().longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
