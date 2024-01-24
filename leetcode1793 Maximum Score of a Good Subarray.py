from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l, r = k, k
        n = len(nums)
        ans = 0
        minOfWindow = nums[k]
        while l >= 0 or r < n:
            ans = max(ans, minOfWindow * (r - l + 1))
            if l == 0 and r == n - 1:
                break
            if l - 1 >= 0 and r + 1 < n:
                if nums[l - 1] > nums[r + 1]:
                    minOfWindow = min(minOfWindow, nums[l - 1])
                    l -= 1
                else:
                    minOfWindow = min(minOfWindow, nums[r + 1])
                    r += 1
            elif l - 1 >= 0:
                minOfWindow = min(minOfWindow, nums[l - 1])
                l -= 1
            else:
                minOfWindow = min(minOfWindow, nums[r + 1])
                r += 1

        return ans


print(Solution().maximumScore(nums=[1, 4, 3, 7, 4, 5], k=3))
print(Solution().maximumScore(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0))
