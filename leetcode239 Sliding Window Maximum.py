from collections import deque
from typing import List

# O(N) decreasing queue/stack solution
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        ans = []
        for i, num in enumerate(nums):
            while stack and i - stack[0][0] + 1 > k:
                stack.popleft()
            while stack and stack[-1][1] <= num:
                stack.pop()
            stack.append([i, num])
            if i >= k - 1:
                ans.append(stack[0][1])

        return ans


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
