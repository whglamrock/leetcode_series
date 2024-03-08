from collections import deque
from typing import List

# 1) nums = nums + nums
# 2) scanning from right to left, using a increasing queue/stack (from right to left) to store the min prefixSum[j]
# in range [i - n // 2, i - 1] ==> prefixSum[i] - min(prefixSum[j]) is the max subarray Sum that ends at i
# 3) when adding element to the increasing queue, we also need to add index so we can pop out the invalid prefix from right
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        nums = nums + nums
        prefixSums = []
        for num in nums:
            if not prefixSums:
                prefixSums.append(num)
            else:
                prefixSums.append(prefixSums[-1] + num)

        n = len(nums)
        increasingQueue = deque()
        for i in range(n - 2, n // 2 - 2, -1):
            while increasingQueue and increasingQueue[0][0] >= prefixSums[i]:
                increasingQueue.popleft()
            increasingQueue.appendleft([prefixSums[i], i])

        ans = -2147483648
        for i in range(n - 1, n // 2 - 1, -1):
            # currPrefixSum is the new prefixSum on the left side we are adding to the increasingQueue
            currPrefixSum = prefixSums[i - n // 2]
            while increasingQueue and increasingQueue[0][0] >= currPrefixSum:
                increasingQueue.popleft()
            increasingQueue.appendleft([currPrefixSum, i - n // 2])

            ans = max(ans, prefixSums[i] - increasingQueue[-1][0])
            # the smallest prefixSum in increasingQueue cannot be i - 1 because in the next
            # for loop it's gonna be deducted from prefixSums[i - 1] which will always == 0
            while increasingQueue and increasingQueue[-1][1] >= i - 1:
                increasingQueue.pop()

        return ans
