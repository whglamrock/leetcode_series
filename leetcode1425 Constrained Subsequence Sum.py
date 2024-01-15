from collections import deque
from typing import List

# A naive O(N * K) DP solution won't work. need to think of using a sliding window of size k
# to store the previous k dp (subsequent sum) values.
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        subseqSumQueue = deque()

        for i in range(n):
            # need to check the queue size
            while i > k and subseqSumQueue and i - subseqSumQueue[0][0] > k:
                subseqSumQueue.popleft()
            if subseqSumQueue:
                dp[i] = max(nums[i], nums[i] + subseqSumQueue[0][1])
            else:
                dp[i] = nums[i]
            while subseqSumQueue and subseqSumQueue[-1][1] < dp[i]:
                subseqSumQueue.pop()
            subseqSumQueue.append([i, dp[i]])

        return max(dp)


print(Solution().constrainedSubsetSum(nums=[10, 2, -10, 5, 20], k=2))
print(Solution().constrainedSubsetSum(nums=[-1, -2, -3], k=1))
print(Solution().constrainedSubsetSum(nums=[10, -2, -10, -5, 20], k=2))
