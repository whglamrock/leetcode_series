from collections import deque
from typing import List

# when dealing with circular array, always just double the array
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
        increasingStack = deque()
        ans = -2147483647
        for i, prefixSum in enumerate(prefixSums):
            while increasingStack and i - increasingStack[0][0] + 1 > n // 2:
                increasingStack.popleft()

            # when i < n // 2, we don't have to worry about left index of the prefix array
            if i < n // 2:
                ans = max(ans, prefixSum)
            if increasingStack:
                ans = max(ans, prefixSum - increasingStack[0][1])

            while increasingStack and increasingStack[-1][1] > prefixSum:
                increasingStack.pop()
            increasingStack.append([i, prefixSum])

        return ans
