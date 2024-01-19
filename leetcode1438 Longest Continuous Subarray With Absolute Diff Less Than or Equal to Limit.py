from collections import deque
from typing import List

# sliding window idea
# keep a decreasing queue and an increasing queue to store the min & max of the subarray
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasingQueue, decreasingQueue = deque(), deque()
        l = 0
        ans = 1
        for r, num in enumerate(nums):
            # add new number to the queue
            while increasingQueue and num <= increasingQueue[-1][1]:
                increasingQueue.pop()
            increasingQueue.append([r, num])
            while decreasingQueue and num >= decreasingQueue[-1][1]:
                decreasingQueue.pop()
            decreasingQueue.append([r, num])

            # make sure the subArray's max diff <= limit
            while increasingQueue and decreasingQueue and decreasingQueue[0][1] - increasingQueue[0][1] > limit:
                l += 1
                while increasingQueue[0][0] < l:
                    increasingQueue.popleft()
                while decreasingQueue[0][0] < l:
                    decreasingQueue.popleft()

            ans = max(ans, r - l + 1)

        return ans


print(Solution().longestSubarray([8, 2, 4, 7], 4))
print(Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5))
print(Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))
print(Solution().longestSubarray([1], 0))
