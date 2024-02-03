from typing import List

# For each nums[i] as the longest edge, find 2 edges within nums[:i] whose sum > nums[i].
# 1) Below two pointer approach guarantees O(N) for finding the all 2 pointers and O(N ^ 2) overall time
# 2) If in real interview we can't think of the 2 pointer approach, fixing a nums[j] as the second longest edge
# and using binary search to find the 3rd edge should be also acceptable; although the overall time will be O(N * N * log(N)).
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        ans = 0
        for i in range(2, n):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    # using nums[r] and all nums[l:r] to form the other 2 edges
                    ans += r - l
                    r -= 1
                else:
                    l += 1

        return ans
