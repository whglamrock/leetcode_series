from collections import deque
from typing import List


# keep a decreasing queue and an increasing queue to store the min & max of the subarray
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasingStack, decreasingStack = deque(), deque()
        l = 0
        ans = 0
        for r, num in enumerate(nums):
            while increasingStack and increasingStack[-1][1] > num:
                increasingStack.pop()
            while decreasingStack and decreasingStack[-1][1] < num:
                decreasingStack.pop()
            increasingStack.append([r, num])
            decreasingStack.append([r, num])
            while decreasingStack[0][1] - increasingStack[0][1] > limit:
                l = min(decreasingStack[0][0], increasingStack[0][0]) + 1
                while increasingStack and increasingStack[0][0] < l:
                    increasingStack.popleft()
                while decreasingStack and decreasingStack[0][0] < l:
                    decreasingStack.popleft()

            ans = max(r - l + 1, ans)

        return ans


print(Solution().longestSubarray([8, 2, 4, 7], 4))
print(Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5))
print(Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))
print(Solution().longestSubarray([1], 0))
